# Healthcare Backend API (Django + DRF + PostgreSQL)

This project implements a simple healthcare backend system with **JWT authentication** using Django, Django REST Framework, and PostgreSQL.  
The backend allows managing **patients, doctors, and their mappings**.

---

## 🔹 Setup Instructions

1. **Clone the repository and install dependencies:**

    ```
    git clone https://github.com/E-cyborg/internshala/tree/main/WhatBytes
    cd healthcare_backend
    pip install -r requirements.txt
    ```

2. **Setup PostgreSQL database in `.env` file:**
    ```
    SECRET_KEY=your_django_secret
    ```

3. **Run migrations and start server:**
    ```
    python manage.py migrate
    python manage.py runserver
    ```

The API will be available at:  
👉 http://127.0.0.1:8000

---

## 🔹 Authentication APIs

1. **Register User**
    ```
    curl -X POST http://127.0.0.1:8000/api/auth/register/ \
      -H "Content-Type: application/json" \
      -d '{
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123"
      }'
    ```

2. **Login User**
    ```
    curl -X POST http://127.0.0.1:8000/api/auth/login/ \
      -H "Content-Type: application/json" \
      -d '{
        "email": "alice@example.com",
        "password": "password123"
      }'
    ```

    Copy the "access" token from response.  
    For the next requests, replace `<ACCESS_TOKEN>` with that token.

---

## 🔹 Patient APIs

3. **Create Patient**
    ```
    curl -X POST http://127.0.0.1:8000/api/patients/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <ACCESS_TOKEN>" \
      -d '{
        "name": "John Doe",
        "age": 30,
        "gender": "M",
        "address": "123 Main St"
      }'
    ```

4. **List Patients**
    ```
    curl -X GET http://127.0.0.1:8000/api/patients/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

5. **Get Patient by ID**
    ```
    curl -X GET http://127.0.0.1:8000/api/patients/1/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

6. **Update Patient**
    ```
    curl -X PUT http://127.0.0.1:8000/api/patients/1/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <ACCESS_TOKEN>" \
      -d '{
        "name": "John Doe",
        "age": 31,
        "gender": "M",
        "address": "New Address 456"
      }'
    ```

7. **Delete Patient**
    ```
    curl -X DELETE http://127.0.0.1:8000/api/patients/1/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

---

## 🔹 Doctor APIs

8. **Create Doctor**
    ```
    curl -X POST http://127.0.0.1:8000/api/doctors/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <ACCESS_TOKEN>" \
      -d '{
        "name": "Dr. Smith",
        "specialization": "Cardiologist",
        "email": "drsmith@example.com",
        "phone": "9876543210"
      }'
    ```

9. **List Doctors**
    ```
    curl -X GET http://127.0.0.1:8000/api/doctors/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

10. **Get Doctor by ID**
    ```
    curl -X GET http://127.0.0.1:8000/api/doctors/1/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

11. **Update Doctor**
    ```
    curl -X PUT http://127.0.0.1:8000/api/doctors/1/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <ACCESS_TOKEN>" \
      -d '{
        "name": "Dr. John Smith",
        "specialization": "Cardiologist",
        "email": "drsmith@example.com",
        "phone": "9999999999"
      }'
    ```

12. **Delete Doctor**
    ```
    curl -X DELETE http://127.0.0.1:8000/api/doctors/1/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

---

## 🔹 Mapping APIs

13. **Assign Doctor to Patient**
    ```
    curl -X POST http://127.0.0.1:8000/api/mappings/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <ACCESS_TOKEN>" \
      -d '{
        "patient": 1,
        "doctor_id": 1
      }'
    ```

14. **List All Mappings**
    ```
    curl -X GET http://127.0.0.1:8000/api/mappings/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

15. **List Doctors for a Patient**
    ```
    curl -X GET http://127.0.0.1:8000/api/mappings/1/doctors/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

16. **Delete a Mapping**
    ```
    curl -X DELETE http://127.0.0.1:8000/api/mappings/1/ \
      -H "Authorization: Bearer <ACCESS_TOKEN>"
    ```

---

## 🔹 Refreshing Access Token

When your access token expires, use the refresh token:

