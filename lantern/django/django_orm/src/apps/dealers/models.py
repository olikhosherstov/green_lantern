from django.db import models
from django.db.models import Index
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=25, unique=True)

    class Meta:
        db_table = 'country'
        ordering = ["name"]
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE,
                                  blank=False, null=False)

    class Meta:
        db_table = 'city'
        ordering = ["name"]
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Dealer(User):
    CityId = models.ForeignKey('City', on_delete=models.DO_NOTHING,
                               blank=True, null=True)

    @property
    def title(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')


class NewsLetter(models.Model):
    email = models.EmailField(max_length=50, unique=True)
