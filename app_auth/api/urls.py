from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),  # DRF's built-in view to obtain auth token // uses username
    path('register/', RegisterView.as_view(), name='register'),
]