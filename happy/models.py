from django.db import models
from django.contrib.auth.models import User

class Created_event(models.Model):
    user_id_creater=models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)
    date=models.DateField(auto_now=False)
    type_of_event=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.TextField(max_length=5000)
    description=models.TextField(max_length=5000,null=True,default=None)
    status_of_creater=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id_creater)

class Accepted_event(models.Model):
    date=models.DateField(auto_now=True)
    user_id_creater=models.ForeignKey(Created_event,default=1,on_delete=models.SET_DEFAULT)
    user_id_accepter=models.ForeignKey(User,default=1,on_delete=models.SET_DEFAULT)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    email=models.TextField(max_length=500)
    accepter_status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id_accepter)


