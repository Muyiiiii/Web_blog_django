# Generated by Django 3.2.9 on 2023-06-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_moment_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Moment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
