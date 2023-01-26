from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class regmodel(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)

class userregmodel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) #username,email,password
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Dealer(models.Model):
    dname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Employee(models.Model):
    e_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    sal = models.CharField(max_length=20)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Medicine(models.Model):
    m_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=30)
    dname = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):
        return self.mname


class Purchase(models.Model):
    pname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phn_no = models.BigIntegerField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()
    total = models.BigIntegerField()

    def __str__(self):
        return self.pname
