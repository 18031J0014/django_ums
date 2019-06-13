from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField 
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    rollno= models.CharField(max_length=10)
    gender = models.CharField(max_length=50,choices=(
        ('male','male'),
        ('female','female')
    ))
    department = models.CharField(max_length=50,choices=(
        ('IT','IT'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('EEE','EEE')
    ))
    address = models.TextField(max_length=100)
    password = models.CharField(max_length=20,default="Student")
    image=models.ImageField(upload_to='images',blank=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']