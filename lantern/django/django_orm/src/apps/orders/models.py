from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField


class Order(models.Model):
    STATUS_PAID = 'Paid'
    STATUS_DEPOSIT = 'Deposit'
    STATUS_EXPECT = 'Expect'
    STATUS_ARCHIVED = 'Archived'

    STATUS_CHOICES = (
        (STATUS_PAID, 'Paid'),
        (STATUS_DEPOSIT, 'Deposit'),
        (STATUS_EXPECT, 'Expect'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=STATUS_EXPECT)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=70)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    message = models.CharField(max_length=255)

    class Meta:
        indexes = [Index(fields=('status',))]
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.status
