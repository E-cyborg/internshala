# Healthcare Backend API (Django + DRF + PostgreSQL)

This project implements a simple healthcare backend system with **JWT authentication** using Django, Django REST Framework, and PostgreSQL.  
The backend allows managing **patients, doctors, and their mappings**.

---

## 🔹 Setup Instructions

1. Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd healthcare_backend
pip install -r requirements.txt
Setup PostgreSQL database in .env file:

ini
Copy
Edit
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret
DEBUG=True
Run migrations and start server:

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
The API will be available at:
👉 http://127.0.0.1:8000

🔹 Authentication APIs
1. Register User
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "email": "alice@example.com",
    "password": "password123"
  }'
2. Login User
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.com",
    "password": "password123"
  }'
✅ Copy the "access" token from response.
For the next requests, replace <ACCESS_TOKEN> with that token.

🔹 Patient APIs
3. Create Patient
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "name": "John Doe",
    "age": 30,
    "gender": "M",
    "address": "123 Main St"
  }'
4. List Patients
bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
5. Get Patient by ID
bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/api/patients/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
6. Update Patient
bash
Copy
Edit
curl -X PUT http://127.0.0.1:8000/api/patients/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "name": "John Doe",
    "age": 31,
    "gender": "M",
    "address": "New Address 456"
  }'
7. Delete Patient
bash
Copy
Edit
curl -X DELETE http://127.0.0.1:8000/api/patients/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
🔹 Doctor APIs
8. Create Doctor
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "name": "Dr. Smith",
    "specialization": "Cardiologist",
    "email": "drsmith@example.com",
    "phone": "9876543210"
  }'
9. List Doctors
bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/api/doctors/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
10. Get Doctor by ID
bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/api/doctors/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
11. Update Doctor
bash
Copy
Edit
curl -X PUT http://127.0.0.1:8000/api/doctors/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "name": "Dr. John Smith",
    "specialization": "Cardiologist",
    "email": "drsmith@example.com",
    "phone": "9999999999"
  }'
12. Delete Doctor
bash
Copy
Edit
curl -X DELETE http://127.0.0.1:8000/api/doctors/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
🔹 Mapping APIs
13. Assign Doctor to Patient
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/mappings/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "patient": 1,
    "doctor_id": 1
  }'
14. List All Mappings
bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/api/mappings/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
15. List Doctors for a Patient
bash
Copy
Edit
curl -X GET http://127.0.0.1:8000/api/mappings/1/doctors/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
16. Delete a Mapping
bash
Copy
Edit
curl -X DELETE http://127.0.0.1:8000/api/mappings/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
🔹 Refreshing Access Token
When your access token expires, use the refresh token:

bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "<REFRESH_TOKEN>"
  }'