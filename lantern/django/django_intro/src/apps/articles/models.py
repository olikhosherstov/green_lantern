from django.conf import settings
from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, verbose_name='Title', db_index=True)
    body = models.TextField(max_length=5000, verbose_name='Article body')
    tags = models.ManyToManyField(to='Tag', related_name='articles', blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )


class Country(models.Model):
    CountryId = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'country'


class City(models.Model):
    CityId = models.AutoField(primary_key=True)
    CityName = models.CharField(max_length=50)
    CountryId = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Menu(models.Model):
    MenuId = models.AutoField(primary_key=True)
    MenuName = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'menu'


class Dish(models.Model):
    DishId = models.AutoField(primary_key=True)
    DishName = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True, null=True)
    recipe = models.TextField(blank=True, null=True)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dish'


class RestaurantMenu(models.Model):
    MenuId = models.ForeignKey('Menu', models.DO_NOTHING, db_column='MenuId', blank=True, null=True)
    DishId = models.ForeignKey('Dish', models.DO_NOTHING, db_column='DishId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RestaurantMenu'


class Restaurant(models.Model):
    RestaurantId = models.AutoField(primary_key=True)
    RestaurantName = models.CharField(max_length=50)
    CountryId = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryId', blank=True, null=True)
    CityId = models.ForeignKey('City', models.DO_NOTHING, db_column='CityId', blank=True, null=True)
    Address = models.CharField(unique=True, max_length=50)
    MenuId = models.ForeignKey('RestaurantMenu', models.DO_NOTHING, db_column='MenuId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Staff(models.Model):
    StaffId = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    BirthDate = models.DateField(blank=True, null=True)
    Profession = models.CharField(max_length=25)
    Skill = models.CharField(max_length=25, blank=True, null=True)
    Salary = models.FloatField(blank=True, null=True)
    RestaurantId = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='RestaurantId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
