from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.UserCreateAPIView.as_view()),
    path('all/', views.UserListAPIView.as_view()),
    path('<int:pk>/', views.UserDetailAPIView.as_view())
]