from django.db import models

# Create your models here.

#user model
class User_model(models.Model):
    id	= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)	
    phone = models.CharField(max_length=16)
    dob	= models.DateField()
    profession = models.CharField(max_length=40)
    address = models.CharField(max_length=255)
    class Meta:
        db_table = "user"


#admin model for admin table data
class Admin_model(models.Model):
    id	= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)	
    phone = models.CharField(max_length=16)
    class Meta:
        db_table = "admin"


#admin model for admin table data
class Stock_model(models.Model):
    id	= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)	
    last = models.FloatField()	
    high = models.FloatField()	
    low	= models.FloatField()	
    change_price = models.FloatField()	
    changePercent = models.FloatField()	
    vol	= models.IntegerField()
    change_time	= models.TimeField()
    change_date = models.DateField()
    details = models.TextField()
    class Meta:
        db_table = "stock"


# for bid
class Bid_model(models.Model):
    id	= models.IntegerField(primary_key=True)
    USERid	= models.IntegerField()
    STOCKid	= models.IntegerField()
    class Meta:
        db_table = "bid"