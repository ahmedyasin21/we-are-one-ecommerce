# Generated by Django 3.1.5 on 2021-02-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='post categories')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_category', verbose_name='post category image')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='shop categories')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_category', verbose_name='shop category image')),
            ],
        ),
    ]
