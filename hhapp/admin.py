# admin.py

from django.contrib import admin
from .models import Donor, Volunteer, Donate, Donee, Needs, Events

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'dob', 'gender', 'age')
    search_fields = ('name', 'email', 'phone_number')

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'donor', 'volunteer_category')
    search_fields = ('donor__email', 'volunteer_category')

class DonateAdmin(admin.ModelAdmin):
    list_display = ('id', 'donor', 'name', 'category', 'count')
    search_fields = ('donor__email', 'name', 'category')

class DoneeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'approved', 'details')
    search_fields = ('name', 'email', 'phone_number')

class NeedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'donee', 'name', 'category', 'count', 'status')
    search_fields = ('donee__email', 'name', 'category', 'status')

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'venue', 'date', 'category', 'donee')
    search_fields = ('name', 'venue', 'category', 'donee__email')

admin.site.register(Donor, DonorAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donate, DonateAdmin)
admin.site.register(Donee, DoneeAdmin)
admin.site.register(Needs, NeedsAdmin)
admin.site.register(Events, EventsAdmin)
