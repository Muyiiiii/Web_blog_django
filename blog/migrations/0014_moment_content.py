# Generated by Django 3.2.9 on 2023-06-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_moment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='moment',
            name='content',
            field=models.TextField(default='无内容', verbose_name='内容'),
        ),
    ]