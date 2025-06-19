from django.urls import path
import api.views as v
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('blogs',v.BlogsView.as_view()),
    path('blog/<int:pk>',v.BlogView.as_view()),
    path('com',v.CommentsView.as_view()),
    path('com/<int:pk>',v.CommentView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pro/',v.ProctedView.as_view())

]
