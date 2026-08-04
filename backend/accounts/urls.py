from django.urls import path
from .views import LoginView, RegisterView, UserProfileView

urlpatterns = [
    path('user/', UserProfileView.as_view(), name="all-users"),
    path('user/<int:pk>/', UserProfileView.as_view(), name="users-detail"),
    path('auth/register/', RegisterView.as_view(), name="register"),
    path('auth/login/', LoginView.as_view(), name="login")
]
