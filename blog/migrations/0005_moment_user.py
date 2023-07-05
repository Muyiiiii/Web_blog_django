# Generated by Django 3.2.9 on 2023-06-04 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0004_auto_20230604_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(upload_to='pic/', verbose_name='图片')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.CharField(max_length=1000, verbose_name='内容')),
                ('author_name', models.CharField(max_length=30, verbose_name='作者')),
                ('email', models.CharField(max_length=100, verbose_name='邮箱')),
                ('kind', models.CharField(max_length=100, verbose_name='类别')),
                ('is_valid', models.BooleanField(default=False, verbose_name='内容是否合法')),
            ],
            options={
                'verbose_name': '帖子库',
                'verbose_name_plural': '帖子库',
                'db_table': 'Moment',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100, verbose_name='邮箱')),
                ('if_login', models.BooleanField(default=False, verbose_name='是否在线')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'User',
            },
        ),
    ]
