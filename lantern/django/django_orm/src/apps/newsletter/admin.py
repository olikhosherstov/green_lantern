from django.contrib import admin

from apps.newsletter.models import NewsLetter


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    pass
