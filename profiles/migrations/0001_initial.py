# Generated by Django 3.1.5 on 2021-02-24 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpeg', upload_to='displays', verbose_name='displays')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='age')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='last_name')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='username')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50, null=True, verbose_name='gender')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email')),
                ('bio', models.CharField(blank=True, max_length=250, null=True, verbose_name='About you')),
                ('website', models.URLField(blank=True, max_length=250, null=True, verbose_name='Website')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('street_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='street address')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='city')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='state')),
                ('zip_code', models.CharField(max_length=50, null=True, verbose_name='zip code')),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
