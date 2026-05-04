from django.db import models
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == '':
            base_slug = slugify(self.name) or 'category'
            slug = base_slug
            counter = 1 
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter+=1
            self.slug = slug
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
        if not self.slug or self.slug.strip() == '':
            base_slug = slugify(self.title) or 'post'
            slug = base_slug
            counter = 1 
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter+=1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 