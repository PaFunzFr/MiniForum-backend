from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentList.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail')
]