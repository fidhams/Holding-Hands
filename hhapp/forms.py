# forms.py

from django import forms
from .models import Donor, Volunteer, Donate, Donee, Needs, Events

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['email', 'password', 'name', 'phone_number', 'dob', 'gender']
        widgets = {
            'password': forms.PasswordInput(),
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['donor', 'volunteer_category', 'volunteer_details']

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['donor', 'name', 'category', 'count', 'image']

class DoneeForm(forms.ModelForm):
    class Meta:
        model = Donee
        fields = ['name', 'email', 'password', 'phone_number', 'address', 'details']
        widgets = {
            'password': forms.PasswordInput(),
        }

class NeedsForm(forms.ModelForm):
    class Meta:
        model = Needs
        fields = ['donee', 'name', 'category', 'count', 'status']

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'venue', 'date', 'category', 'description', 'donee']
