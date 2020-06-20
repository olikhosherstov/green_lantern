
from django.db import models
from django.db.models import Index, UniqueConstraint
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from apps.cars.managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel


class Color(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        constraints = [
            UniqueConstraint(fields=('name',), name='unique-color')
        ]
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=32)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        constraints = [
            UniqueConstraint(fields=('name',), name='unique-car-brand')
        ]
        verbose_name = _('Car brand')
        verbose_name_plural = _('Car brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        constraints = [
            UniqueConstraint(fields=('name', 'brand'), name='unique-car-model')
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class CarEngine(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ('name',)
        indexes = [Index(fields=('name',)),]
        verbose_name = _('Car Engine')
        verbose_name_plural = _('Car Engines')

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=12, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Fuel Type')
        verbose_name_plural = _('Fuel Types')

    def __str__(self):
        return self.name


class Car(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    objects = CarManager.from_queryset(CarQuerySet)()
    color = models.ForeignKey(to='Color', on_delete=models.SET_NULL, null=True, blank=False)
    dealer = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE, null=True, blank=False)
    model = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True, blank=False)
    engineType = models.ForeignKey(to='CarEngine', on_delete=models.SET_NULL, null=True, blank=False)
    price = MoneyField(max_digits=9, decimal_places=2, default_currency="USD", null=True)
    fuelType = models.ForeignKey(to='FuelType', on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    doors = models.PositiveSmallIntegerField(default=4)
    capacity = models.PositiveSmallIntegerField(default=100)
    gearCase = models.PositiveSmallIntegerField(default=4)
    number = models.CharField(max_length=16, unique=True)
    slug = models.SlugField(max_length=75)
    sittingPlaces = models.PositiveSmallIntegerField(default=4)
    firstRegistrationDate = models.DateField(auto_now_add=False, null=True, blank=False)
    enginePower = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    extra_title = models.TextField(max_length=50, null=True)

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

        indexes = [Index(fields=["status", ])]

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.title


class Property(models.Model):
    name = models.CharField(max_length=55)
    category = models.CharField(max_length=55)
    car = models.ManyToManyField("Car", related_name="properties")


class CarProperty(models.Model):
    property = models.ForeignKey(to='Property', on_delete=models.DO_NOTHING, null=True, blank=False)
    car = models.ForeignKey(to='Car', on_delete=models.DO_NOTHING, null=True, blank=False)
