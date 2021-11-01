# Generated by Django 3.1.5 on 2021-03-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20210223_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='tag_line',
            field=models.CharField(blank=True, default='We are one.', max_length=100, null=True, verbose_name='Tag Line'),
        ),
        migrations.AlterField(
            model_name='shopprofile',
            name='shop_bg',
            field=models.ImageField(default='shop_default.jpeg', upload_to='shop_back_grounds', verbose_name='Shop Logo'),
        ),
        migrations.AlterField(
            model_name='shopprofile',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Shop Title'),
        ),
    ]
