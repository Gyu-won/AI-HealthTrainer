from django.db import models
from django.db import connections
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.timezone import now
import pymysql
# Create your models here.
class Goal(models.Model):
    start = models.DateField()
    stop = models.DateField()
    goal = models.CharField(max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        db_table="goal"
    
class Exercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='null')
    
    def _str_(self):
        return self.name
    
    class Meta:
        db_table="exercise"
        
class Workout(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    count = models.SmallIntegerField(("Count"))
    start_time = models.DateTimeField(("Start Time"), auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(("End Time"), auto_now=False, auto_now_add=False)
    
    class Meta:
        db_table = "Workout"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    my_photo = models.ImageField(default='pp.png', upload_to='dp/')
    first_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=False, null=False, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=14)

    joined = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
