# Generated by Django 3.1.5 on 2021-03-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0009_auto_20210318_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopprofile',
            name='shop_category',
            field=models.CharField(blank=True, max_length=150, verbose_name='shop catagory'),
        ),
    ]