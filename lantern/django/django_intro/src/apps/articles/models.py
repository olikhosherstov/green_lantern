from django.conf import settings
from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, verbose_name='title', db_index=True)
    body = models.TextField(max_length=5000, verbose_name='article_body')
    tags = models.ManyToManyField(to='Tag', related_name='articles', blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='Articles'
    )


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        dbTable = 'Country'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)
    country_id = models.ForeignKey('Country', models.DO_NOTHING, db_column='country_id', blank=True, null=True)

    class Meta:
        managed = False
        dbTable = 'City'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        dbTable = 'Menu'


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True, null=True)
    recipe = models.TextField(blank=True, null=True)
    weight = models.IntegerField()

    class Meta:
        managed = False
        dbTable = 'Dish'


class RestaurantMenu(models.Model):
    menu_id = models.ForeignKey('Menu', models.DO_NOTHING, db_column='menu_id', blank=True, null=True)
    dish_id = models.ForeignKey('Dish', models.DO_NOTHING, db_column='dish_id', blank=True, null=True)

    class Meta:
        managed = False
        dbTable = 'RestaurantMenu'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50)
    country_id = models.ForeignKey('Country', models.DO_NOTHING, db_column='country_id', blank=True, null=True)
    city_id = models.ForeignKey('City', models.DO_NOTHING, db_column='city_id', blank=True, null=True)
    address = models.CharField(unique=True, max_length=50)
    menu_id = models.ForeignKey('RestaurantMenu', models.DO_NOTHING, db_column='menu_id', blank=True, null=True)

    class Meta:
        managed = False
        dbTable = 'Restaurant'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    profession = models.CharField(max_length=25)
    skill = models.CharField(max_length=25, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    restaurant_id = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='restaurant_id', blank=True, null=True)

    class Meta:
        managed = False
        dbTable = 'Staff'
