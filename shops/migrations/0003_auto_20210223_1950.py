# Generated by Django 3.1.5 on 2021-02-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_shopprofile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='amazon',
            field=models.URLField(blank=True, null=True, verbose_name='amazon'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='daraz',
            field=models.URLField(blank=True, null=True, verbose_name='daraz'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='facebook'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='pinterest',
            field=models.URLField(blank=True, null=True, verbose_name='pinterest'),
        ),
        migrations.AddField(
            model_name='shopprofile',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='twitter'),
        ),
    ]
