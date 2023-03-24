from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra):
        user = self.model(username=username, email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra):
        admin = self.model(
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True,
            **extra
        )
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    def create_user(self, username, email, password):
        return self._create_user(username, email, password)