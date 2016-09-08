from django.contrib import admin
from blog.models import Post    # модель из blog/models.py

# Register your models here.
admin.site.register(Post)