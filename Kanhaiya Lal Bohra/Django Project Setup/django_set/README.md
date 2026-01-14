# Django REST, Celery & Telegram Bot Boilerplate

This project is a modern Django REST Framework (DRF) setup, including JWT authentication, a simple blog/comments API, Celery integration with Redis for background tasks, and a Telegram Bot integration to collect user info. The project is organized for clarity and easy extensibility.

## Features

- **Django REST Framework**: Build APIs quickly and securely.
- **JWT Authentication**: Secure endpoints using JSON Web Tokens.
- **User Registration & Login**: Standard web-based login and registration forms.
- **Environment-Based Configuration**: Secrets and sensitive settings are loaded from environment variables for security.
- **Celery + Redis**: Asynchronous background task processing with Redis as the broker (e.g., sending welcome emails after registration).
- **Telegram Bot Integration**: Receives `/start` commands, collects user Telegram usernames, and stores them in your Django database.
- **Production-Ready Settings**: `DEBUG` is set to `False` and other best practices are followed for deployment.

## Project Structure

```
django_set/
├── api/            # API endpoints (blog, comments, etc.)
├── media/          # Models for blogs and comments
├── register/       # User registration, login, related tasks
├── django_set/     # Project settings, celery, urls
├── templates/      # HTML templates for authentication
└── manage.py
```

## Getting Started

1. **Clone the project**
    ```bash
    git clone https://github.com/E-cyborg/internshala.git
    cd 'Kanhaiya Lal Bohra/Django Project Setup/django_set'
    ```

2. **Set up your Python environment**
    ```bash
    python -m venv .venv
    .venv/Script/activate
    pip install -r requirements.txt
    ```

3. **Configure environment variables**

    Create a `.env` file in the project root and define:
    ```
    SECRET_KEY=your-secret-key
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
    # For PostgreSQL or others, add DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

    EMAIL_HOST_USER=your-email@gmail.com
    EMAIL_HOST_PASSWORD=your-app-password

    ```

4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run Redis** (required for Celery)
    ```
    redis-server
    ```

7. **Start Celery worker**
    ```
    celery -A django_set worker --loglevel=info
    ```

8. **Run the development server**
    ```bash
    python manage.py runserver
    ```

9. **Start the Telegram Bot**
    [Click here to chat with @kinyborgbot](https://t.me/kinyborgbot)
    - The bot will respond to the `/start` command and save the user's Telegram username to your database.

## API Overview

- **Public Endpoints**
    - `POST /api/com` and `GET /api/com`: Create/list comments (no authentication required)
- **Protected Endpoints** (JWT required)
    - `POST /api/blogs`, `GET /api/blogs`: Create/list blogs
    - `GET /api/blog/<int:pk>`: Retrieve, update, or delete a specific blog
    - `POST /api/pro/`: Example protected endpoint
    - **JWT Token:**  
      - Obtain: `POST /api/token/` with `username` & `password`
      - Refresh: `POST /api/token/refresh/` with refresh token

## Celery Tasks

- **Welcome Email**:  
  When a user logs in, a background task sends a welcome email using Celery and Redis.

## Telegram Bot

- Listens for `/start` commands.
- Saves the user's Telegram username to your Django database.
- For more logic, extend the `telegrambot` app!


## Authentication (Web)

- **Register**: `/register/sign/`
- **Login**: `/register/login/`
- **Logout**: `/register/logout/`

## Production Notes

- Make sure `DEBUG=False` in `settings.py`.
- Use strong, unique values for all secrets in your environment.
- Configure allowed hosts in `ALLOWED_HOSTS`.
- Set up your SMTP credentials for email functionality.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

Made with ❤️ using Django, DRF, Celery, and Telegram Bot API.