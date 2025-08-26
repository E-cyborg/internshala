# 🧠 Comment API — Internship Assessment

This project is submitted as part of the internship assessment for the role of **Associate Software Engineer (Python / React)** at Better Software. The task was to implement backend CRUD APIs for managing **comments on a task**, using proper software engineering practices.

---

## ✅ Task 1: Backend APIs (Completed)

### 📌 Features

- Create, Read, Update, and Delete comments associated with a task.
- Follows RESTful principles and clean code structure.
- Includes automated tests to validate functionality.
- Built using Django + Django REST Framework. *(or Flask, if applicable — update as needed)*

---

## 📁 Project Structure (Key Parts)

├── models.py # Comment model (linked to Task)
├── serializers.py # Comment serializer for DRF
├── views.py # CRUD API views for comments
├── urls.py # Routes for API endpoints
├── tests.py # Automated tests for the API

---

## 🔄 API Endpoints

| Method | Endpoint                      | Description              |
|--------|-------------------------------|--------------------------|
| GET    | `/tasks/<task_id>/comments/`  | List comments for task   |
| POST   | `/tasks/<task_id>/comments/`  | Create a new comment     |
| PUT    | `/comments/<comment_id>/`     | Update a comment         |
| DELETE | `/comments/<comment_id>/`     | Delete a comment         |

*Endpoints may vary slightly depending on the router/view setup.*

---


```bash
python manage.py runserver
