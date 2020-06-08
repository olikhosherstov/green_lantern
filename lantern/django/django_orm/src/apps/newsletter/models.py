from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseDateAuditModel


class NewsLetter(BaseDateAuditModel):
    email = models.EmailField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['email']
        verbose_name = _("Newsletter")
        verbose_name_plural = _("Newsletters")

    def __str__(self):
        return self.email
