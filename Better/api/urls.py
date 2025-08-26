from django.urls import path
from . import views
urlpatterns =[
    path('comment/<pk>',views.CommentView.as_view()),
    path('comments',views.CommentsView.as_view()),

    
    path('task/<pk>',views.TaskView.as_view()),
    path('tasks',views.TasksView.as_view()),
]