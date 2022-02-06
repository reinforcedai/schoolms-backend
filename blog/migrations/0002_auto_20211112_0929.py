# Generated by Django 3.2.9 on 2021-11-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='social_link',
        ),
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='instagram',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='linkedin',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='youtube',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(blank=True, to='blog.Author'),
        ),
        migrations.DeleteModel(
            name='SocialLink',
        ),
    ]
