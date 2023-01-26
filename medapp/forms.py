from django import forms
from django.contrib.auth.models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['cust_id', 'fname', 'lname', 'phn_no', 'address', 'med_name', 'qty']

class regform(forms.Form):
    name=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)

class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)