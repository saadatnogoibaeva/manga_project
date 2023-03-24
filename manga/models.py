from django.db import models
from common.models import BaseModel


class Genre(BaseModel):
    title = models.CharField(max_length=250, verbose_name="Имя жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title


class Manga(BaseModel):
    title_id = models.IntegerField(
        unique=True, verbose_name="Индентификатор", null=True, blank=True
    )
    en_name = models.CharField(max_length=200, verbose_name="Название на английском")
    ru_name = models.CharField(max_length=200, verbose_name="Название на русском")
    slug = models.SlugField(
        max_length=250, null=True, blank=True, verbose_name="Индентификатор"
    )
    image = models.URLField(
        null=True, verbose_name="Ссылка на картинку из другого источника"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    chapters_quantity = models.PositiveIntegerField(
        null=True, verbose_name="Кол-во глав"
    )
    issue_year = models.PositiveIntegerField(null=True, verbose_name="Дата выпуска")
    type = models.CharField(max_length=100, verbose_name="Тип комикса")
    genre = models.ManyToManyField(Genre, verbose_name="Жанр манги")
    likes = models.PositiveIntegerField(
        verbose_name="Кол-во лайков", null=True, blank=True
    )
    views = models.PositiveIntegerField(
        verbose_name="Кол-во просмотров", null=True, blank=True
    )
    rating = models.FloatField(default=0.0, blank=True, verbose_name="Рейтинг")

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манга"

    def __str__(self):
        return self.en_name