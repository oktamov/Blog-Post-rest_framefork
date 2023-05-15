# from django.urls import path
#
# from blogs.views import PostListView, PostDetailView, PostLike, CommentCreateAPIView
#
# urlpatterns = [
#     path('post-list/', PostListView.as_view(), name='post_list'),
#     path('post-detail/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
#     path('post-detail/<slug:slug>/like/', PostLike.as_view(), name='post_likes'),
#     path('comments/create/', CommentCreateAPIView.as_view(), name='comment_create'),
# ]
from django.urls import path
from .views import PostList, PostDetail, CommentCreate, CommentList, PostLike

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post-detail/<slug:slug>/like/', PostLike.as_view(), name='post_likes'),
    path('posts/<int:post_pk>/comments/create/', CommentCreate.as_view(), name='comment_create'),
    path('posts/<int:post_pk>/comments/', CommentList.as_view(), name='comment_list'),
]
