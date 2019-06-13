from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Results(models.Model):
    name = models.CharField(max_length=20)
    roolno = models.CharField(max_length=10)
    department = models.CharField(max_length=50,choices=(
        ('IT','IT'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('EEE','EEE')
    ))
    semister = models.CharField(max_length=50,choices=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8')
    ))
    subjects = models.CharField(max_length=50,choices=(
        ('M1','M1'),
        ('MM','MM'),
        ('CP','CP'),
        ('JAVA','JAVA'),
        ('DBMS','DBMS'),
        ('DS','DS'),
        ('OS','OS'),
        ('WP','WP')
    ))
    marks = models.IntegerField(default=0)
    pass_fail = models.CharField(max_length=5,default='null')
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']