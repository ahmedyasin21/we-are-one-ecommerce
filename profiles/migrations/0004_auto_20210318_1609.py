# Generated by Django 3.1.5 on 2021-03-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_userprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='personal email'),
        ),
    ]
