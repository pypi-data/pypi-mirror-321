from io import BytesIO
import webbrowser
from typing import List
from textual import on, work
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.geometry import Spacing
from textual.message import Message
from textual.reactive import reactive
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button, LoadingIndicator, Static
from rich_pixels import Pixels
from PIL import Image
import httpx

from alexandria.book import Book


class DownloadButton(Button):
    def __init__(self, book: Book):
        super().__init__(
            label=f"🔽 {book.extension.upper()} ({book.size})",
            tooltip="Download " + book.extension.upper(),
        )
        self.book = book
        self.styles.background_tint = self.color_for_extension()

    @on(Button.Pressed)
    async def on_button_pressed(self, event: Button.Pressed):
        event.stop()
        self.download_book()

    @work
    async def download_book(self) -> None:
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                if self.book.should_open_browser:
                    webbrowser.open(self.book.download_url)
                    return

                self.notify(f"Download started for {self.book.title}")
                r = await client.get(self.book.download_url)

                filename = self.book.title.replace(
                    " ", "-") + "." + self.book.extension

                with open(filename, "wb") as f:
                    f.write(r.content)

                self.notify(f"Downloaded book to {filename}")
        except Exception as ex:
            self.log("Failed to download book: " + str(ex))
            self.notify("Failed to download book", severity="error")

    def color_for_extension(self) -> str:
        match self.book.extension.upper():
            case "PDF":
                return "red"
            case "EPUB":
                return "lightblue"
            case "AZW3":
                return "yellow"
            case "MOBI":
                return "cyan"
            case _:
                return "gray"


class ImageWidget(Static):
    def __init__(self, pixels: Pixels):
        super().__init__()
        self.pixels = pixels

    def on_mount(self):
        self.update(self.pixels)


class BookView(Widget):
    pixels: reactive[Pixels | None] = reactive(None, recompose=True)

    def __init__(self, book: Book):
        super().__init__()
        self.book = book

    class LoadImage(Message):
        def __init__(self, url: str):
            super().__init__()
            self.url = url

    def on_mount(self):
        self.log("image url: " + self.book.image_url)
        self.post_message(self.LoadImage(self.book.image_url))

    async def on_book_view_load_image(self, event: LoadImage):
        event.stop()
        self.download_image(event.url)

    @work
    async def download_image(self, url: str):
        try:
            async with httpx.AsyncClient(verify=False) as client:
                self.log(f'Downloading image: {url}')
                r = await client.get(url)
                size = 32, 32
                if r.status_code == 200:
                    img = Image.open(BytesIO(r.content))
                    img.thumbnail(size, Image.Resampling.LANCZOS)
                    self.pixels = Pixels.from_image(img)
                else:
                    self.log(f"Failed to fetch image {
                             url} for book {self.book.title}")
        except Exception as ex:
            self.log(
                f'There was an error while fetching the book image: {ex.args}')

    def compose(self) -> ComposeResult:
        with Horizontal(classes="book-view-container"):
            with Vertical(classes="book-metadata"):
                yield Static(f"[b]{self.book.title}[/b]", classes="book-title")
                yield Static(", ".join(self.book.authors), classes="book-authors")
                yield DownloadButton(self.book)
            with Container(classes="book-image"):
                if self.pixels is not None:
                    yield ImageWidget(self.pixels)
                else:
                    yield LoadingIndicator()


class BooksView(Widget):
    books: reactive[List[Book]] = reactive([], recompose=True)

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            for book in self.books:
                yield BookView(book)
