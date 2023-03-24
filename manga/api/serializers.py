from rest_framework import serializers
from ..models import Manga, Genre
from users.models import Comment, User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["username"] = instance.username
        if instance.image_file is None:
            data["image"] = instance.image
        data["image"] = instance.image_file
        return data


class CommentSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()
    text = serializers.CharField(max_length=255)

    class Meta:
        model = Comment
        fields = ["id", "user", "text"]
        extra_kwargs = {"author": {"read_only": True}}

    def get_count_of_likes(self, obj):
        return Comment.objects.filter(comment=obj).count()


class CommentAddSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    text = serializers.CharField(max_length=250)
    manga = serializers.SlugRelatedField(slug_field=Manga.slug, read_only=True)

    class Meta:
        model = Comment
        fields = ["text", "manga"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "title",
        )


class ManagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = (
            "id",
            "en_name",
            "slug",
            "image",
            "description",
            "chapters_quantity",
            "issue_year",
            "type",
            "genre",
            "likes",
            "views",
            "rating",
        )


class MangaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = (
            "id",
            "en_name",
            "ru_name",
            "image",
            "description",
            "chapters_quantity",
            "issue_year",
            "type",
            "genre",
            "likes",
            "views",
            "rating",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["comments_count"] = instance.manga_comments.count()
        return data