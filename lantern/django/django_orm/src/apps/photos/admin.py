from django.contrib import admin
from imagekit.admin import AdminThumbnail
from apps.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)
    image_display = AdminThumbnail(image_field='image')
    image_display.short_description = 'Photo.car.name'

    readonly_fields = ['image']
