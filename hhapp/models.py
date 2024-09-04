# models.py

from django.db import models
from datetime import date


class Donor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    email = models.EmailField('Email Address', primary_key=True)
    password = models.CharField('Password', max_length=100)
    name = models.CharField('Full Name', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=15)
    dob = models.DateField('Date of Birth')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __str__(self):
        return f"{self.name} (Email: {self.email}, Age: {self.age}, Gender: {self.get_gender_display()})"
    


class Volunteer(models.Model):
    COMPANIONSHIP_SUPPORT = 'CS'
    MENTORING_TUTORING = 'MT'
    ACTIVITIES_EVENT_MANAGEMENT = 'AEM'
    HEALTH_WELLNESS_SUPPORT = 'HWS'
    ADVOCACY_OUTREACH = 'AO'
    SPECIAL_PROJECTS = 'SP'
    OTHERS = 'O'
    
    VOLUNTEER_CATEGORY_CHOICES = [
        (COMPANIONSHIP_SUPPORT, 'Companionship and support'),
        (MENTORING_TUTORING, 'Mentoring and Tutoring'),
        (ACTIVITIES_EVENT_MANAGEMENT, 'Activities or event management'),
        (HEALTH_WELLNESS_SUPPORT, 'Health and Wellness support'),
        (ADVOCACY_OUTREACH, 'Advocacy and outreach'),
        (SPECIAL_PROJECTS, 'Special Projects'),
        (OTHERS, 'Others'),
    ]

    id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    volunteer_category = models.CharField(max_length=3, choices=VOLUNTEER_CATEGORY_CHOICES, default=OTHERS)
    volunteer_details = models.TextField('Volunteer Details', blank=True)

    def __str__(self):
        return f"Volunteer ID: {self.id}, Donor: {self.donor.email}, Category: {self.get_volunteer_category_display()}"

class Donate(models.Model):
    CLOTHING = 'Clothing'
    HYGIENE_PRODUCTS = 'Hygiene Products'
    SCHOOL_SUPPLIES = 'School Supplies'
    HOUSEHOLD_ITEMS = 'Household items'
    MEDICAL_SUPPLIES = 'Medical Supplies'
    TOYS_AND_GAMES = 'Toys and Games'
    ELECTRONICS = 'Electronics'
    FURNITURE = 'Furniture'
    BOOKS_AND_MAGAZINES = 'Books and Magazines'
    OTHERS = 'Others'
    
    CATEGORY_CHOICES = [
        (CLOTHING, 'Clothing'),
        (HYGIENE_PRODUCTS, 'Hygiene Products'),
        (SCHOOL_SUPPLIES, 'School Supplies'),
        (HOUSEHOLD_ITEMS, 'Household items'),
        (MEDICAL_SUPPLIES, 'Medical Supplies'),
        (TOYS_AND_GAMES, 'Toys and Games'),
        (ELECTRONICS, 'Electronics'),
        (FURNITURE, 'Furniture'),
        (BOOKS_AND_MAGAZINES, 'Books and Magazines'),
        (OTHERS, 'Others'),
    ]

    id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, to_field='email')
    name = models.CharField('Donation Name', max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHERS)
    count = models.PositiveIntegerField('Item Count')
    image = models.ImageField(upload_to='donation_images/', blank=True, null=True)

    def __str__(self):
        return f"Donation ID: {self.id}, Donor: {self.donor.email}, Name: {self.name}, Category: {self.get_category_display()}"




class Donee(models.Model):
    email = models.EmailField('Email', primary_key=True)
    name = models.CharField('Name', max_length=100)
    password = models.CharField('Password', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=15)
    address = models.CharField('Address', max_length=255)
    approved = models.CharField(
        'Approved',
        max_length=3,
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No')
        ],
        default='No'
    )
    details = models.TextField('Details', blank=True, null=True)

    def __str__(self):
        return self.name



class Needs(models.Model):
    CLOTHING = 'Clothing'
    HYGIENE_PRODUCTS = 'Hygiene Products'
    SCHOOL_SUPPLIES = 'School Supplies'
    HOUSEHOLD_ITEMS = 'Household items'
    MEDICAL_SUPPLIES = 'Medical Supplies'
    TOYS_AND_GAMES = 'Toys and Games'
    ELECTRONICS = 'Electronics'
    FURNITURE = 'Furniture'
    BOOKS_AND_MAGAZINES = 'Books and Magazines'
    OTHERS = 'Others'
    
    CATEGORY_CHOICES = [
        (CLOTHING, 'Clothing'),
        (HYGIENE_PRODUCTS, 'Hygiene Products'),
        (SCHOOL_SUPPLIES, 'School Supplies'),
        (HOUSEHOLD_ITEMS, 'Household items'),
        (MEDICAL_SUPPLIES, 'Medical Supplies'),
        (TOYS_AND_GAMES, 'Toys and Games'),
        (ELECTRONICS, 'Electronics'),
        (FURNITURE, 'Furniture'),
        (BOOKS_AND_MAGAZINES, 'Books and Magazines'),
        (OTHERS, 'Others'),
    ]

    URGENT = 'Urgent'
    NOT_URGENT = 'Not Urgent'
    
    STATUS_CHOICES = [
        (URGENT, 'Urgent'),
        (NOT_URGENT, 'Not Urgent'),
    ]

    id = models.AutoField(primary_key=True)
    donee = models.ForeignKey(Donee, on_delete=models.CASCADE, to_field='email')
    name = models.CharField('Need Name', max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHERS)
    count = models.PositiveIntegerField('Item Count')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NOT_URGENT)

    def __str__(self):
        return f"Need ID: {self.id}, Donee: {self.donee.email}, Name: {self.name}, Category: {self.get_category_display()}"


class Events(models.Model):
    COMPANIONSHIP_SUPPORT = 'Companionship and support'
    MENTORING_TUTORING = 'Mentoring and Tutoring'
    EVENT_MANAGEMENT = 'Activities or event management'
    HEALTH_WELLNESS = 'Health and Wellness support'
    ADVOCACY_OUTREACH = 'Advocacy and outreach'
    SPECIAL_PROJECTS = 'Special Projects'
    OTHERS = 'Others'
    
    CATEGORY_CHOICES = [
        (COMPANIONSHIP_SUPPORT, 'Companionship and support'),
        (MENTORING_TUTORING, 'Mentoring and Tutoring'),
        (EVENT_MANAGEMENT, 'Activities or event management'),
        (HEALTH_WELLNESS, 'Health and Wellness support'),
        (ADVOCACY_OUTREACH, 'Advocacy and outreach'),
        (SPECIAL_PROJECTS, 'Special Projects'),
        (OTHERS, 'Others'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField('Event Name', max_length=100)
    venue = models.CharField('Venue', max_length=200)
    date = models.DateField('Event Date')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=OTHERS)
    description = models.TextField('Description')
    donee = models.ForeignKey(Donee, on_delete=models.CASCADE, to_field='email')

    def __str__(self):
        return f"Event: {self.name}, Venue: {self.venue}, Date: {self.date}, Category: {self.get_category_display()}"
