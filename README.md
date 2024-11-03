# Blog API

A simple blog API built with FastAPI, SQLAlchemy, and SQLite. This API supports CRUD operations, including creating, reading, updating, and deleting blog posts. It also includes a search endpoint that allows users to search for posts by keywords.

## Features
- Create, retrieve, update, and delete blog posts
- Search posts by title, content, category, author, or date
- Automatic timestamp formatting for created posts

## Endpoints

### Home
- **`GET /`**
    - Description: Welcome message.

### Posts
- **`POST /posts`**
    - Description: Create a new blog post.
    - Request Body:
      ```json
      {
        "title": "Sample Post",
        "content": "This is the content of the post",
        "author": "Author Name",
        "category": "Category Name"
      }
      ```
    - Response:
      ```json
      {
        "id": 1,
        "title": "Sample Post",
        "content": "This is the content of the post",
        "author": "Author Name",
        "category": "Category Name",
        "created_at": "YYYY-MM-DD HH:MM:SS"
      }
      ```

- **`GET /posts`**
    - Description: Retrieve all blog posts.
    - Response: List of all posts in the database.

- **`GET /posts/{id}`**
    - Description: Retrieve a single blog post by ID.
    - Parameters:
      - `id` (int): ID of the post.
    - Response: Details of the specified post.

- **`PUT /edit-post/{id}`**
    - Description: Update a blog post by ID.
    - Parameters:
      - `id` (int): ID of the post to update.
    - Request Body:
      ```json
      {
        "title": "Updated Title",
        "content": "Updated content",
        "author": "Updated Author",
        "category": "Updated Category"
      }
      ```
    - Response: Updated details of the specified post.

- **`DELETE /delete-post/{id}`**
    - Description: Delete a blog post by ID.
    - Parameters:
      - `id` (int): ID of the post to delete.
    - Response: Confirmation message.

- **`GET /posts/search?term=keyword`**
    - Description: Search blog posts by title, content, author, category, or created date.
    - Query Parameter:
      - `term` (str): Keyword to search for.
    - Response: List of posts matching the search term.

## Getting Started

### Prerequisites
- Python 3.9+
- SQLite (or any SQL database if you update the configuration)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Incognitol07/basic-blog-api.git
    cd basic-blog-api
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    - Ensure SQLite is configured in `models.py`.
    - The database will be created automatically when you run the app.

4. Run the application:
    ```bash
    uvicorn app:app --reload
    ```
   - The API will be accessible at `http://127.0.0.1:8000`.

5. Go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Project Structure
basic-blog-api \
├── main.py # Entry point for the API \
├── models.py # Database models and ORM setup \
├── config.py # Database configuration (if applicable) \
├── requirements.txt # Project dependencies \
└── README.md # Project documentation\