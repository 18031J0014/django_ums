from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.
class Administration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50,choices=(
        ('male','male'),
        ('female','female')
    ))
    password = models.CharField(max_length=20,default="Administration")
    image=models.ImageField(upload_to='images',blank=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']