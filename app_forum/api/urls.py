from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail')
]