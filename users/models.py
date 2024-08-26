from django.db import models

# Create your models here.
class user(models.Model):
    pseudo=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=128)
    creat_at=models.DateField(auto_now_add=True)
