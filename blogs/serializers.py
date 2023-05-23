from rest_framework import serializers

from blogs.models import Post, Comment, LikeDislike


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "blog", "user", "body", 'parent')


class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "blog", "user", "body", 'parent')
        read_only_fields = ("id",)


class BlogLikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.LikeType.choices)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'author', 'category', 'comments', 'likes', 'dislikes']
