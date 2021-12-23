from django.db import models
from users import models as user_models


class Post(models.Model):
    body = models.CharField(max_length=280)
    author = models.ForeignKey(user_models.User, on_delete=models.RESTRICT)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    user = models.ForeignKey(user_models.User, on_delete=models.RESTRICT)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'user']
