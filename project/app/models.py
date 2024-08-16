from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField()

class Register_Manger(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    def __str__(self):
        return self.user.username

class Reg_guest(models.Model):
    fullname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=30)
    Adress=models.TextField()
    def __str__(self):
        return self.fullname




class Resort_packs(models.Model):
    my_choice = (
        ('family','family'),
        ('friends','friends'),
        ('couple','couple'),
        ('comapnya pack','company pack'),
        ('get together','get together'),
        ('students pack','students pack'),
    )
    select_pack= models.CharField(max_length=50,choices=my_choice)
    price=models.IntegerField()
    details=models.TextField()
    no_of_rooms = models.IntegerField()
    img = models.ImageField(upload_to='images/')

class Booking(models.Model):
    user=models.ForeignKey(Reg_guest,on_delete=models.CASCADE)
    resort=models.ForeignKey(Resort_packs,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
class order(models.Model):
    books=models.ForeignKey(Booking, on_delete=models.CASCADE)
    
    








    





