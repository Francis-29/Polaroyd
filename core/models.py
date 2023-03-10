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

    @property
    def imageURL(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return url

    @property
    def bannerURL(self):
        try:
            url = self.banner.url
        except:
            url = ''
        return url


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True, upload_to='posts')
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def likes_count(self):
        try:
            count = self.like_set.all().count()
        except:
            count = 0
        return count

    def __str__(self):
        return self.author.username + " - " + self.caption


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
