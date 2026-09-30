from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()


class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int


class Book(BookCreate):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", publication_year=1962),
}


@app.get("/")
def read_root():
    # TODO: Return a JSON welcome message.
    pass


@app.get("/books", response_model=list[Book])
def read_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    # TODO: Return the requested book, or raise HTTPException with status 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    # TODO: Assign a unique ID, save the new book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def replace_book(book_id: int, book_data: BookCreate):
    # TODO: Replace the requested book, or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    # TODO: Delete the requested book or raise HTTPException with status 404.
    pass
