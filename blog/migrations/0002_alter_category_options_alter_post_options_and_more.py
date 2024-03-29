# Generated by Django 5.0.1 on 2024-01-24 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["title"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={
                "ordering": ["title"],
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=250, unique=True, verbose_name="Алиас"),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.CharField(max_length=100, verbose_name="Автор"),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="posts",
                to="blog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True, verbose_name="Содержимое"),
        ),
        migrations.AlterField(
            model_name="post",
            name="photo",
            field=models.ImageField(
                blank=True, upload_to="media/%Y/%m/%\\d", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique=True, verbose_name="Алиас"),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="blog.tag", verbose_name="Теги"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(max_length=250, unique=True, verbose_name="Алиас"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Наименование"),
        ),
    ]
