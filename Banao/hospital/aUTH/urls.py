from django.urls import path
from aUTH import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', v.loginView, name="login"),
    path('', v.user_view, name="user"),
    path('logout/', v.LogoutView, name="logout"),
    path('sign/', v.RegisterView, name="sign"),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
