from rest_framework import generics, permissions, status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from paginations import CustomPageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentCreateSerializer, CommentSerializer


class PostLike(APIView):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        user = request.user
        if user in post.liked.all():
            post.liked.remove(user)
            return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
        else:
            post.liked.add(user)
            return Response({'detail': 'Post liked.'}, status=status.HTTP_200_OK)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-id')[:20]
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['title']
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        post = generics.get_object_or_404(Post, pk=post_pk)
        serializer.save(post=post, author=self.request.user)


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_pk)
