from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('login/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view()),
    path('register', views.UserView.as_view()),

    path('notes',views.NotesView.as_view()),
    path('note/<pk>',views.NoteView.as_view())
]

# DB schema → show 2 tables:
# users (id, username, password_hash)
# notes (id, user_id, title, content, created_at, updated_at)
# Auth choice → say JWT (stateless, good for APIs).
# List routes (method + path + request/response JSON):
# POST /auth/register → register user
# POST /auth/login → get JWT
# POST /notes → create note
# GET /notes → list all user notes
# GET /notes/{id} → get one note
# PUT /notes/{id} → update note
# DELETE /notes/{id} → delete note