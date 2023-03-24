from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager
from common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(null=True, unique=True, blank=True, verbose_name="Почта")
    username = models.CharField(max_length=50, unique=True)
    phone = PhoneNumberField(null=True, blank=True, verbose_name="Номер телефона")
    image = models.URLField(
        null=True, blank=True, verbose_name="Ссылка на картинку из другого источника"
    )
    image_file = models.ImageField(
        default="back_media/manga_user.png",
        upload_to="back_media/uploaded_media",
        null=True,
        blank=True,
        verbose_name="Картинка",
    )
    favorite_manga = models.ManyToManyField(
        "manga.Manga",
        null=True,
        blank=True,
        related_name="user_favorite_manga",
        verbose_name="Избранное",
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Комментатор")
    manga = models.ForeignKey(
        "manga.Manga",
        on_delete=models.CASCADE,
        related_name="manga_comments",
        verbose_name="Манга",
    )
    text = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Текст"
    )

    def __str__(self):
        return f"{self.user} Прокомментровал {self.manga}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"



