


from enum import Enum
from queue import Empty
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.
# class BookType(Enum):
#    ten_days = 1
#    five_days = 2
#    two_days = 3
 
class Property(models.Model):
   id = models.AutoField(primary_key=True, editable=False)
   room = models.SmallIntegerField(_("room"),null=False)
   floor = models.FloatField(_("floor"),null=False)
   property_type = models.CharField(_("property_type"),max_length=100, null=False)
#    square_meter = models.SmallIntegerField(_("square_meter"),null=False)
   street=models.CharField(_("street"),max_length=100, null=False)
   neighbourhood=models.CharField(_("neighbourhood"),max_length=100, null=False)
   location = models.CharField(_("location"),max_length=100, null=False)
#    street_number=models.SmallIntegerField(_("street_number"),null=False)
   price= models.BigIntegerField(_("price"),null=False)
   # image=models.ImageField(null=True,blank=True,
   #                          default='/placeholder.jpg')

   def __str__(self):
       return self.room +","+ self.floor+","+ self.property_type+","+ self.neighbourhood+","+ self.location+","+ self.street+","+ self.price
   def __repr__(self):
        return self.__str__() 

class Project(models.Model):
   type_project= models.CharField(_("type_project"),max_length=100, null=False)
   size_project= models.SmallIntegerField(_("size_project"),null=False)
   company= models.CharField(_("company"),max_length=100, null=False)
   dates= models.BigIntegerField(_("dates"),null=True, blank=True)
   location= models.CharField(_("location"),max_length=100, null=False)
   neighbourhood=models.CharField(("neighbourhood"),max_length=100, null=True)
   # street = models.CharField(_("street"),max_length=100, null=False)
   # street_number = models.SmallIntegerField(_("street_number"), null=False)
   value= models.FloatField(_("value"),null=False)
   
   def __str__(self):
       return self.type_project +","+self.size_project +","+self.company +","+self.dates +","+self.value +","+self.loaction +","+self.street +","+self.street_number
   def __repr__(self):
        return self.__str__() 


