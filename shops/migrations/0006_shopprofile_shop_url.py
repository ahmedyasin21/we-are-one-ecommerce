# Generated by Django 3.1.5 on 2021-03-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_shopprofile_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='shop_url',
            field=models.URLField(blank=True, null=True, verbose_name='Shop Url'),
        ),
    ]
