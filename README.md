# FastAPI htmx with Client Hot Reload

This project is a demonstration of how to implement client-side hot reloading using FastAPI and Arel.

## Usage

To run the project, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/somenoe/fastapi-htmx-with-client-hot-reload.git
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Build the CSS:

    ```sh
    make tailwind
    ```

4. Run the server:

    ```sh
    make run
    ```

## Project Structure

```
├── templates
│   ├── input.css
│   ├── index.html
│   └── ...
├── static
│   ├── styles.css
│   └── htmx.min.js
└── main.py
```

## Inspiration

This project was inspired by the following example:

-   [Automatic browser reloading in FastAPI](https://gist.github.com/vrslev/6d0602bfa939a01844f645c608afb85a)

## Tech Stack

This project uses the following technologies:

-   [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs.
-   [Arel](https://github.com/florimondmanca/arel/tree/master/example) - A hot-reloading client for web development.
-   [HTMX](https://htmx.org/docs/) - A JavaScript library that allows you to access AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, using attributes.
-   [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework for rapidly building custom designs.
