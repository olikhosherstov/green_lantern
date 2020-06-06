from django.contrib import admin

from apps.cars.models import Car, Color, CarModel, CarBrand, CarEngine, FuelType


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'extra_title',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarEngine)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)



