# Generated by Django 3.2.9 on 2021-11-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_count',
            field=models.IntegerField(default=0),
        ),
    ]
