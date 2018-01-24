from django.contrib import admin

from .models import Shelter, Guardian, Request


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_num_guardians',
    )


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'shelter',
        'phone_number',
    )


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'time',
        'get_location',
        'name',
        'phone_number',
        'platform',
    )
