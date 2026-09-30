import requests

API_URL = "https://jsonplaceholder.typicode.com/todos?userId=1"


def get_todos():
    """Return todo items from the public API, or an empty list on failure."""
    # TODO: Send a GET request and return the decoded JSON data.
    return []


def display_todos(todos):
    """Print each todo title and its completion status."""
    # TODO: Print [x] for completed items and [ ] for incomplete items.
    pass


def count_todos(todos):
    """Return the number of completed and incomplete todo items."""
    # TODO: Count items using their Boolean "completed" value.
    return 0, 0


def main():
    todos = get_todos()
    display_todos(todos)

    completed, incomplete = count_todos(todos)
    print(f"Completed: {completed}")
    print(f"Incomplete: {incomplete}")


if __name__ == "__main__":
    main()
