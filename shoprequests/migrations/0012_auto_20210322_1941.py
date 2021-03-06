# Generated by Django 3.1.5 on 2021-03-22 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoprequests', '0011_auto_20210322_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoprequest',
            name='address_proof',
            field=models.CharField(choices=[('1', 'Licence'), ('2', 'Government id')], max_length=50, verbose_name='address proof'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='address_proof_img',
            field=models.ImageField(upload_to='address_proof_img', verbose_name='Address Verification'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='age',
            field=models.IntegerField(default=2, verbose_name='age'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='city',
            field=models.CharField(max_length=50, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='id_proof',
            field=models.CharField(choices=[('1', 'Licence'), ('2', 'Government id'), ('3', 'Passport')], max_length=50, verbose_name='id proof'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='id_proof_img',
            field=models.ImageField(upload_to='id_proof_img', verbose_name='ID Verification'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='nationality',
            field=models.CharField(max_length=50, verbose_name='nationality'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='request_approve',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Cancel', 'Cancel')], max_length=50, verbose_name='request approval'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='shop_address',
            field=models.CharField(max_length=50, verbose_name='shop address'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='state',
            field=models.CharField(max_length=50, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='street_address',
            field=models.CharField(max_length=50, verbose_name='street address'),
        ),
        migrations.AlterField(
            model_name='shoprequest',
            name='zip_code',
            field=models.CharField(max_length=50, verbose_name='zip code'),
        ),
    ]
