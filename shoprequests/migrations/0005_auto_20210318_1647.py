# Generated by Django 3.1.5 on 2021-03-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoprequests', '0004_auto_20210318_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoprequest',
            name='id_proof',
            field=models.CharField(choices=[('1', 'Licence'), ('2', 'Government id'), ('3', 'Passport')], max_length=50, null=True, verbose_name='id_proofs'),
        ),
        migrations.AddField(
            model_name='shoprequest',
            name='id_proof_img',
            field=models.ImageField(null=True, upload_to='id_proof_img', verbose_name='Account Verification'),
        ),
    ]
