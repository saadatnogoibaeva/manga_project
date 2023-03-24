from rest_framework.exceptions import APIException


class UsernameExistsException(APIException):
    default_code = "username_exists"
    default_detail = "User with the same username already exists"
    status_code = 400


class UserNotFoundException(APIException):
    default_code = "not_found"
    default_detail = "User not found"
    status_code = 404


class FavoriteMangaExistsException(APIException):
    default_code = "favorite_manga_exists"
    default_detail = "The manga is already in my favorites"
    status_code = 400


class MangaNotFoundException(APIException):
    default_code = "not_found"
    default_detail = "Manga not found"
    status_code = 404