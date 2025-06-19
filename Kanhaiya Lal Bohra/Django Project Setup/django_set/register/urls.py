from django.urls import path
import register.views  as V
urlpatterns = [
    path('login/',V.LoginView,name='login'),
    path('sign/',V.UserRegisterView,name='register'),
    path('',V.home,name='home'),
    path('logout/',V.LogoutView,name='logout')
]
