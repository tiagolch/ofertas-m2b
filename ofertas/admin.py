from django.contrib import admin
from .models import Cities, States, Apps, Svas, Ofertas


@admin.register(States)
class StatesAdmin(admin.ModelAdmin):
    list_display = ['uf']


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ['cities']


@admin.register(Apps)
class AppsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Svas)
class SvasAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Ofertas)
class OfertasAdmin(admin.ModelAdmin):
    list_display = ['promocao']
    list_filter = ['state', 'is_special', 'price']