from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=60)
    link = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    author_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.title} {self.link} {self.creation_date} {self.author_name}"

    def get_absolute_url(self):
        return f"/"

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    username = models.CharField(max_length=255)
    comments = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    name = models.ManyToManyField(Posts, related_name='title_post')

    def __str__(self):
        return f"{self.username} {self.comments} {self.name}"

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'
