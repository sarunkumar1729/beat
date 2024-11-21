from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      trainer_id = models.IntegerField()
      trainer_name = models.CharField(max_length=255)
      address = models.CharField(max_length=255)
      department = models.CharField(max_length=255)
      age = models.IntegerField()
      gender = models.CharField(max_length=255)
      phone = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      married = models.BooleanField()
      salary = models.IntegerField(null=True)
      joining_date = models.DateField()
      
      
      