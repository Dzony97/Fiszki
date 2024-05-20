from django.urls import path
from .views import RegisterView, ListUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', ListUserView.as_view(), name='users-list'),
]