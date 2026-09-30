# 📘 Assignment: Using Web APIs with Python

## 🎯 Objective

Learn how programs communicate with web services by sending an HTTP request with Python and reading JSON data from a public API.

## 📝 Tasks

### 🛠️ Fetch Data from a Web API

#### Description

Complete the `get_todos()` function so it requests todo items for user 1 from the JSONPlaceholder API.

#### Requirements
Completed program should:

- Send a `GET` request to `https://jsonplaceholder.typicode.com/todos?userId=1` using the `requests` library.
- Return the decoded JSON data as a Python list.
- Return an empty list when the request does not succeed.

### 🛠️ Display Todo Items

#### Description

Complete the `display_todos()` function so it prints each todo item's title and completion status.

#### Requirements
Completed program should:

- Call `get_todos()` to retrieve the data.
- Print each todo title with either `completed` or `not completed`.
- Produce readable output such as:
  ```text
  [x] delectus aut autem
  [ ] quis ut nam facilis et officia qui
  ```

### 🛠️ Count Completed Todos

#### Description

Add a summary to the program that reports how many todos are complete and how many remain incomplete.

#### Requirements
Completed program should:

- Count completed todos using the Boolean `completed` value from each JSON object.
- Print the completed count and incomplete count.
- Keep the counting logic in a separate function named `count_todos()`.
