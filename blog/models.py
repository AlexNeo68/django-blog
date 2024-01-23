from enum import unique
import os
from django.db import models
from django.urls import reverse

from config.settings import BASE_DIR

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Алиас')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})
    

    class Meta:
        ordering = ['title']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Алиас')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Алиас')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    author = models.CharField(max_length=100, verbose_name='Автор')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    photo = models.ImageField(upload_to='media/%Y/%m/%\d', blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True, verbose_name='Теги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']

    
