from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserDetails(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', default='img/default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Personal Information
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Contact Information
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

    # Medical Information
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    pre_existing_conditions = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)
    relationship_with_emergency_contact = models.CharField(max_length=50, blank=True, null=True)

    # Insurance Information (if applicable)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    policy_number = models.CharField(max_length=50, blank=True, null=True)
    tpa_details = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class documents(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    document_name=models.CharField(max_length=50)
    document=models.FileField(upload_to='documents', max_length=100)

    def __str__(self):
        return str(self.user)
