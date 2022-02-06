# Generated by Django 3.2.9 on 2021-11-12 09:24

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=2000, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ShareImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('alt', models.CharField(max_length=200)),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(max_length=512)),
                ('twitter', models.URLField(max_length=512)),
                ('instagram', models.URLField(max_length=512)),
                ('youtube', models.URLField(max_length=512)),
                ('linkedin', models.URLField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.CharField(max_length=200)),
                ('favicon', models.ImageField(upload_to='')),
                ('metaTitle', models.CharField(max_length=200)),
                ('metaDescription', models.CharField(max_length=200)),
                ('share_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.shareimage')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='emma', max_length=200)),
                ('last_name', models.CharField(default='emma', max_length=200)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=256)),
                ('photo', models.ImageField(blank=True, max_length=200, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('social_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.sociallink')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=2000)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('slug', models.SlugField(max_length=2000, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Drafted'), (1, 'Published')], default=0)),
                ('author', models.ManyToManyField(blank=True, null=True, to='blog.Author')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('published_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
