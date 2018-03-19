from django.db import models
from django.contrib.auth.models import User
from django.db.models import DecimalField, DateField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='media/images', blank=True)


    def __str__(self):
        return self.user.username

class Picture(models.Model):
    name = models.CharField(max_length=100, unique=True,null=True)
    owner = models.CharField(max_length=100)
    NumberOfRates = models.IntegerField(default=0)
    avgrate = DecimalField(max_digits=2, decimal_places=1,default=0)



    class Meta:
        verbose_name_plural = 'Pictures'

    def __str__(self):  # For Python 2,use __unicode__too
        return self.name

