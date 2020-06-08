# Generated by Django 3.0.6 on 2020-06-08 11:57

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('CityId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dealers.City')),
            ],
            options={
                'verbose_name': 'Dealer',
                'verbose_name_plural': 'Dealers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='country_name_3bb090_idx'),
        ),
        migrations.AddField(
            model_name='city',
            name='countryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealers.Country'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['name'], name='city_name_88111b_idx'),
        ),
    ]
