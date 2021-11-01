# Generated by Django 3.1.5 on 2021-02-19 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoprequests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoprequest',
            name='requested_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoprequest', to=settings.AUTH_USER_MODEL),
        ),
    ]
