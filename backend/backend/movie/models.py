from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.TextField()
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movies')
    admin_post = models.BooleanField(default=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def str(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.content