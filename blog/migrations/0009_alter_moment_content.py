# Generated by Django 3.2.9 on 2023-06-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_moment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='内容'),
        ),
    ]
