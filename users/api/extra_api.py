from rest_framework import serializers
from ..models import User
from manga.models import Manga


class FavoriteMangaAPI(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = (
            "id",
            "en_name",
            "slug",
            "image",
            "issue_year",
            "type",
        )