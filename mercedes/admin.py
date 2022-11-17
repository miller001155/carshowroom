from django.contrib import admin

from .models import *


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('stamp', 'providers', 'price')
    search_fields = ('^stamp',)
    # search_fields = ('=stamp',)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')
    list_filter = ('title',)
