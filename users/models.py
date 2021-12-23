from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Username is required.')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    last_login = models.DateTimeField(default=timezone.now)
    last_activity = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username
