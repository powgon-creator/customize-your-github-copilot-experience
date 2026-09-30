# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for a book collection using FastAPI. Practice defining API routes, validating request data with Pydantic models, and using HTTP methods and status codes to manage resources.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up the FastAPI application and create a simple endpoint that confirms the API is running.

#### Requirements
Completed program should:

- Create a FastAPI application named `app` in the provided starter code.
- Define a `GET /` endpoint that returns a JSON welcome message.
- Install the packages listed in `requirements.txt` and run the API with `uvicorn starter-code:app --reload`.


### 🛠️ Read Books from the API

#### Description
Use a Pydantic model and the provided in-memory collection to let clients retrieve books.

#### Requirements
Completed program should:

- Define a book model with an integer ID, title, author, and publication year, and a request model for new book details without an ID.
- Implement `GET /books` to return all books and `GET /books/{book_id}` to return one book.
- Return an HTTP 404 response when the requested book ID does not exist.


### 🛠️ Manage Books with CRUD Routes

#### Description
Add routes that let clients create, replace, and delete books in the collection.

#### Requirements
Completed program should:

- Implement `POST /books` to add a book, assign it a unique ID, and return HTTP 201.
- Implement `PUT /books/{book_id}` to replace an existing book and return HTTP 404 if the ID does not exist.
- Implement `DELETE /books/{book_id}` to remove an existing book and return HTTP 204, or HTTP 404 if the ID does not exist.
