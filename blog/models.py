from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(unique=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)        

    class Meta:
        verbose_name_plural = 'Categories'

class News(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=512)
    content = RichTextField(blank=True, null=True,)
    image = models.ImageField(upload_to='uploads/', blank=True)
    author = models.CharField(max_length=225, blank=True, null=True,)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,)
    slug = models.SlugField(unique=True, max_length=2000)
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(News, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-published_at']
        verbose_name_plural = 'News And Events'
