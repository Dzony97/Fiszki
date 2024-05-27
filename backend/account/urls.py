from django.urls import path
from .views import RegisterView, ListUserView, CustomTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', ListUserView.as_view(), name='users-list'),
    path('api/token/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]