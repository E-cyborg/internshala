# 🧠 Comment API — Internship Assessment

This project is submitted as part of the internship assessment for the role of **Associate Software Engineer (Python / React)** at Better Software. The task was to implement backend CRUD APIs for managing **comments on a task**, using proper software engineering practices.

---

## ✅ Task 1: Backend APIs (Completed)

### 📌 Features

- Create, Read, Update, and Delete comments associated with a task.
- Follows RESTful principles and clean code structure.
- Includes automated tests to validate functionality.
- Built using **Django + Django REST Framework**.

---

## 📁 Project Structure (Key Files)

├── models.py # Comment model (linked to Task)
├── serializers.py # Comment serializer for DRF
├── views.py # CRUD API views for comments
├── urls.py # Routes for API endpoints
├── tests.py # Automated tests for the API


---

## 🔄 API Endpoints

| Method   | Endpoint                        | Description                    |
|----------|----------------------------------|--------------------------------|
| `GET`    | `/api/comments/`                | Retrieve all comments          |
| `POST`   | `/api/comments/`                | Create a new comment           |
| `PUT`    | `/api/comments/<comment_id>/`   | Update an existing comment     |
| `DELETE` | `/api/comments/<comment_id>/`   | Delete a comment               |

---

## 🧪 Running the Project

Make sure your virtual environment is activated and dependencies are installed.

Start the development server:

```bash
python manage.py runserver
