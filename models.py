from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class stud(models.Model):
    name = models.CharField(max_length=255,null=True)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    pincode = models.IntegerField()
    repair = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)


class just_img(models.Model):
    other = models.OneToOneField(User,on_delete=models.CASCADE,null = True)
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    phone = models.BigIntegerField()

    def __str__(self):
        return f"{self.name}"