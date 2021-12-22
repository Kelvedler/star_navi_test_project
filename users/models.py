from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username
