from rest_framework import serializers
from ..services import UserService
from ..models import User, Comment
from .extra_api import FavoriteMangaAPI
from manga.models import Manga


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5, max_length=35)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=50)
    phone = serializers.CharField(min_length=13, max_length=13)
    image_file = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "phone",
            "email",
            "password",
            "image_file",
        )


class SignInSerializer(serializers.Serializer):
    login = serializers.CharField(min_length=3, max_length=35)
    password = serializers.CharField(min_length=3, max_length=50)


class ProfileSerializer(serializers.ModelSerializer):
    favorite_manga = FavoriteMangaAPI(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "favorite_manga"]


class AddToFavoriteSerializer(serializers.ModelSerializer):
    favorite_manga = serializers.SlugRelatedField(slug_field=Manga.slug, read_only=True)

    class Meta:
        model = Manga
        fields = ("favorite_manga",)