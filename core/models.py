from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    bio = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', default='profile_pics/avatar.png')
    banner = models.ImageField(null=True, blank=True, upload_to='banners')
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True, upload_to='posts')
    likes_count = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author + self.caption[20:]
