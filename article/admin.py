from django.contrib import admin
from article.models import Post, Category


admin.site.register(Category)
admin.site.register(Post)
