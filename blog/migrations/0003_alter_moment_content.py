# Generated by Django 3.2.9 on 2023-06-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_moment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='内容'),
        ),
    ]
