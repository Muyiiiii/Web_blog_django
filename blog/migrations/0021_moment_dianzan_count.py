# Generated by Django 3.2.9 on 2023-06-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='moment',
            name='dianzan_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
