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
from .views import PostList, PostDetail, PostCreateView, CommentListCreateView, \
    CommentDetailView, BlogLikeDislikeView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<slug:slug>/like/', BlogLikeDislikeView.as_view(), name='post_likes'),
    path("posts/<slug:slug>/comments/", CommentListCreateView.as_view(), name="comment_list_create"),
    # path("posts/<slug:slug>/comments/", CommentDetailView.as_view(), name="blog_detail"),
    # path('posts/<int:pk>/comments/create/', CommentCreate.as_view(), name='comment_create'),
    # path('posts/<int:pk>/comments/', CommentList.as_view(), name='comment_get'),
]
