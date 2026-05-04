from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name 

class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, 
        related_name='posts', null=True
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='photo/', null=True, blank=True
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            original_slug = self.slug
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter+=1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 