from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import User, Comment
from .services import UserService
from users.api.serializers import (
    SignInSerializer,
    SignUpSerializer,
    AddToFavoriteSerializer,
    ProfileSerializer,
)
from manga.models import Manga
from common.exceptions import UserNotFoundException, MangaNotFoundException


class SignUpView(generics.CreateAPIView):
    queryset = UserService.model.objects.all()
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            UserService.create_user(serializer.validated_data)
            return response.Response(
                data={"message": "Register successfully"},
                status=status.HTTP_201_CREATED,
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(generics.GenericAPIView):
    queryset = UserService.model.objects.filter(is_deleted=False).filter(
        is_active=False
    )
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data["login"], password=serializer.data["password"]
            )
            return response.Response(
                data=UserService.generate_token(user=user), status=status.HTTP_200_OK
            )

        return response.Response(data=serializer.errors)


class FavoriteMangaApiView(generics.CreateAPIView):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = AddToFavoriteSerializer

    def get(self, request, username):
        try:
            user = get_object_or_404(User, username=username)
            serializer = ProfileSerializer(user, many=False)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            raise UserNotFoundException()

    def post(self, request, slug):
        try:
            user = self.request.user
            manga = get_object_or_404(Manga, slug=slug)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                UserService.add_to_favorite(user, manga)

                return response.Response("OK")

            return response.Response(serializer.errors)
        except:
            MangaNotFoundException()

    def delete(self, request, slug):
        try:
            user = self.request.user
            manga = get_object_or_404(Manga, slug=slug)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                UserService.remove_from_favorite(user, manga)

                return response.Response("OK")

            return response.Response(serializer.errors)
        except:
            MangaNotFoundException()


class GetUserFavoritesMangaView(generics.GenericAPIView):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = ProfileSerializer

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = self.serializer_class(user, many=False)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            raise UserNotFoundException()


