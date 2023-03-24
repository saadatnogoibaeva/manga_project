from django.urls import path
from .views import SignInView, SignUpView, GetUserFavoritesMangaView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("<str:username>/favorites/", GetUserFavoritesMangaView.as_view()),
]