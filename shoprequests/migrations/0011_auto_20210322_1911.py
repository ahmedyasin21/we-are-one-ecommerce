# Generated by Django 3.1.5 on 2021-03-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoprequests', '0010_auto_20210318_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoprequest',
            name='id_proof',
            field=models.CharField(choices=[('1', 'Licence'), ('2', 'Government id'), ('3', 'Passport')], max_length=50, null=True, verbose_name='id proofs'),
        ),
    ]
