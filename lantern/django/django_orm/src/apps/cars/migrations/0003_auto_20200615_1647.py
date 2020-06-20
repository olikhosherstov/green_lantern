# Generated by Django 3.0.6 on 2020-06-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200608_1157'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='carengine',
            name='unique-car-engine',
        ),
        migrations.AlterField(
            model_name='carengine',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
