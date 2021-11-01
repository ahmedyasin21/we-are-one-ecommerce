# Generated by Django 3.1.5 on 2021-02-19 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_address', models.CharField(max_length=255, verbose_name='shop address')),
                ('title', models.CharField(max_length=50, verbose_name='shop')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date')),
                ('shop_bg', models.ImageField(default='shop_default.jpeg', upload_to='shop_back_grounds', verbose_name='Shop background image')),
                ('customers', models.ManyToManyField(related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='coutomers')),
                ('customers_favorite', models.ManyToManyField(related_name='customers_favorite', to=settings.AUTH_USER_MODEL, verbose_name='customers favorite')),
                ('shop_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.shopcategory', verbose_name='shop category')),
                ('shop_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
