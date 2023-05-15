from rest_framework import serializers

from blogs.models import Post, Comment, Tag


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ("id", "content", 'author')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    tag = PostTagSerializer()

    class Meta:
        model = Post
        fields = '__all__'














# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')
#
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#
# class NestedCommentSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')
#
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#
# class PostSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')
#     comments = NestedCommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'author', 'comments']
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
#
#
# class PostListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         # fields = ['title', 'slug', 'body', 'author', 'image', 'video', 'tag', 'views', 'pub_year']
#         fields = '__all__'
#
#     # def to_representation(self, instance):
#     #     data = super().to_representation(instance)
#     #     data["comment"] = CommentSerializer(instance.comment).data
#     #     return data
#
# # class PostSerializer(serializers.ModelSerializer):
# #     comments = CommentSerializer(many=True, read_only=True)
# #
# #     class Meta:
# #         model = Post
# #         fields = ('id', 'title', 'body', 'comments')
# #
# #     def to_representation(self, instance):
# #         data = super().to_representation(instance)
# #         data["comments"] = CommentSerializer(instance.comment).data
# #         return data
