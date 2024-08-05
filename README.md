# Django Book Hub

Django Book Hub is a web application for managing books, recommendations, comments, and user interactions. Users can view and add books, make recommendations, comment on books, and like books and comments. The application integrates with the Google Books API to fetch book details and provides an interactive platform for users to engage with content.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Guide to Set Up Google Books API](#guide-to-set-up-google-books-api)
- [Models](#models)
- [Views](#views)
- [URLs](#urls)
- [Forms](#forms)
- [Running the Project](#running-the-project)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **User Authentication**: Allows users to log in, log out, and register.
- **Book Management**: Users can add and view books with details such as title, author, description, cover image, rating, genre, and published date.
- **Recommendations**: Users can make and view book recommendations.
- **Comments**: Users can add comments on books and view existing comments.
- **Likes**: Users can like books and comments.
- **Replies**: Users can reply to comments.
- **Book Search**: Search for books using the Google Books API and view detailed information.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/VarunGit2022/Book-Hub.git
    cd django-book-hub
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up the Database**:
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the Application**: Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/api/) to see the application in action.

## Configuration

### Google Books API Key
Add your Google Books API key to the Django settings. Create a file named `.env` in the root of your project and add the following line:

```bash
GOOGLE_BOOKS_API_KEY=your_google_books_api_key
