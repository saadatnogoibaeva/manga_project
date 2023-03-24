from .utils import Scrap, create_genre
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Parsing manga"

    def handle(self, *args: any, **options: any) -> object:
        create_genre(self)
        print("---------------Genre created---------------")
        Scrap.scrap_users()
        print("---------------Users created---------------")
        Scrap.scrap_manga()
        # # print("---------------Manga created---------------")
        # Scrap.scrap_comments()
        # print("---------------Comments created---------------")