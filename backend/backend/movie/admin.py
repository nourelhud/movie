from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movies, Post, Comment,Users
admin.site.register(Users)
admin.site.register(Movies)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
