from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import LikeDislike
from blogs.serializers import CommentsDetailSerializer, \
    BlogLikeDislikeSerializer
from custom_permission import IsOwnerOrReadOnly

from paginations import CustomPageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')[:20]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['title']
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.order_by("-id")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentsDetailSerializer
        return CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = "id"
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CommentsDetailSerializer
        return CommentSerializer


class BlogLikeDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BlogLikeDislikeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = BlogLikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        type_ = serializer.validated_data.get("type")
        type_detail = ''
        if type_ == '1':
            type_detail = 'liked'
        if type_ == '-1':
            type_detail = 'unliked'
        user = request.user
        blog = Post.objects.filter(slug=self.kwargs.get("slug")).first()
        if not blog:
            raise Http404
        like_dislike_blog = LikeDislike.objects.filter(blog=blog, user=user).first()
        if like_dislike_blog and like_dislike_blog.type == type_:
            like_dislike_blog.delete()
        else:
            LikeDislike.objects.update_or_create(blog=blog, user=user, defaults={"type": type_})
        data = {"type": type_, "detail": type_detail}
        return Response(data)
