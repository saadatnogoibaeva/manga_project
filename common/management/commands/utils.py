from manga.models import Genre, Manga
from users.models import User, Comment

import requests
import random


class Scrap:
    url = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
    url_comments = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    }
    domen = "https://remanga.org"
    media_domen = "https://remanga.org"

    @classmethod
    def scrap_users(cls):
        for page in range(10, 100):
            url = f"https://api.remanga.org/api/activity/comments/?title_id=80{str(page)}{str(page)}&page={str(page)}&ordering=&count=20"

            response = requests.get(url=url, headers=cls.HEADERS)
            data = response.json()
            for i in data["content"]:
                User.objects.get_or_create(
                    username=i["user"]["username"],
                    image=cls.media_domen + i["user"]["avatar"]["high"],
                    password="useruser123",
                )
                if User.objects.filter(username=i["user"]["username"]).exists():
                    continue

    @classmethod
    def scrap_comments(cls):
        manga_instance = Manga.objects.all()
        if len(manga_instance) > 0:
            while manga_instance.count() < 4000:
                for i in range(1, 100):
                    instance = Manga.objects.all().values_list("title_id", flat=True)
                    for i in instance:
                        url = f"https://api.remanga.org/api/activity/comments/?title_id={i}&page=2&ordering=&count=20"
                        response = requests.get(url=url, headers=cls.HEADERS)
                        data = response.json()
                        for h in Manga.objects.filter(title_id=i):
                            for i in data["content"]:
                                try:
                                    Comment.objects.create(
                                        user=random.choice(User.objects.all()),
                                        text=i["text"],
                                        manga=h,
                                    )
                                except TypeError:
                                    continue
            return f"Comments count over 3999"
        print("Can't find manga")

    @classmethod
    def scrap_manga(cls):
        for i in range(1, 1000):
            url = (
                "https://api.remanga.org/api/titles/recommendations/?&count=20&page="
                + str(i)
            )
            request = requests.get(url=url, headers=cls.HEADERS)
            request_data = request.json()

            for item in request_data["content"]:
                global url2
                url2 = f"https://api.remanga.org/api/titles/" + item["dir"] + "/"
                genre_filter_set = item["genres"]
                manga = Manga.objects.create(
                    title_id=item["id"],
                    en_name=item["en_name"],
                    ru_name=item["rus_name"],
                    slug=item["dir"],
                    image=cls.media_domen + item["cover_high"],
                    type=item["type"],
                    issue_year=item["issue_year"],
                    rating=item["avg_rating"],
                    views=item["total_views"],
                    likes=item["total_votes"],
                    chapters_quantity=item["count_chapters"],
                )
                for i in genre_filter_set:
                    global genre_filter_name
                    genre_filter_name = i["name"]

                    manga.genre.add(*Genre.objects.filter(title=genre_filter_name))
                detail_request = requests.get(url=url2, headers=cls.HEADERS)
                detail_data = detail_request.json()
                try:
                    created_manga = Manga.objects.filter(
                        slug=detail_data["content"]["dir"]
                    )
                except:
                    continue
                for m in created_manga:
                    description = detail_data["content"]["description"]
                    manga = Manga.objects.filter(en_name=m)
                    manga.update(description=description)


def create_genre(self, *args, **kwargs):
    try:
        Genre.objects.get_or_create(title="Боевик")
        Genre.objects.get_or_create(title="Гарем")
        Genre.objects.get_or_create(title="Детектив")
        Genre.objects.get_or_create(title="Гарем")
        Genre.objects.get_or_create(title="Гендерная интрига")
        Genre.objects.get_or_create(title="Героическое фэнтези")
        Genre.objects.get_or_create(title="Детектив")
        Genre.objects.get_or_create(title="Дзёсэй")
        Genre.objects.get_or_create(title="Додзинси")
        Genre.objects.get_or_create(title="Драма")
        Genre.objects.get_or_create(title="Игра")
        Genre.objects.get_or_create(title="История")
        Genre.objects.get_or_create(title="Киберпанк")
        Genre.objects.get_or_create(title="Кодомо")
        Genre.objects.get_or_create(title="Комедия")
        Genre.objects.get_or_create(title="Махо-сёдзё")
        Genre.objects.get_or_create(title="Меха")
        Genre.objects.get_or_create(title="Мистика")
        Genre.objects.get_or_create(title="Мурим")
        Genre.objects.get_or_create(title="Научная фантастика")
        Genre.objects.get_or_create(title="Повседневность")
        Genre.objects.get_or_create(title="Постапокалиптика")
        Genre.objects.get_or_create(title="Приключения")
        Genre.objects.get_or_create(title="Психология")
        Genre.objects.get_or_create(title="Романтика")
        Genre.objects.get_or_create(title="Сверхъестественное")
        Genre.objects.get_or_create(title="Сёдзё")
        Genre.objects.get_or_create(title="Сёдзё-ай")
        Genre.objects.get_or_create(title="Сёнэн")
        Genre.objects.get_or_create(title="Сёнэн-ай")
        Genre.objects.get_or_create(title="Спорт")
        Genre.objects.get_or_create(title="Сэйнэн")
        Genre.objects.get_or_create(title="Трагедия")
        Genre.objects.get_or_create(title="Триллер")
        Genre.objects.get_or_create(title="Ужасы")
        Genre.objects.get_or_create(title="Фантастика")
        Genre.objects.get_or_create(title="Фэнтези")
        Genre.objects.get_or_create(title="Школа")
        Genre.objects.get_or_create(title="Элементы юмора")
        Genre.objects.get_or_create(title="Этти")
        Genre.objects.get_or_create(title="Юри")
        Genre.objects.get_or_create(title="Яой")
    except:
        return False