from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import *
from .models import *

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cps=a.cleaned_data['cpassword']

            if ps==cps:
                b=regmodel(name=nm,username=un,email=em,phone=ph,password=ps)
                b.save()
                return render(request,"index.html")
            else:
                return HttpResponse("Password not matching")
        else:
            return render(request,"registration.html")
    else:
        return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            ps = a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                if username==i.username and ps==i.password:
                    email=i.email
                    return render(request,'index.html',{'username':username,'email':email})
            else:
                return HttpResponse('login failed')
    else:
            return render(request,'login.html')



def dealerform(request):
    dict = {'add': True, }
    return render(request, 'dealer.html', dict)


def dealerforminsert(request):
    try:
        dealer = Dealer()
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request,'new.html')
    return render(request, 'index.html')


def dealerformupdate(request, id):
    try:
        dealer = Dealer.objects.get(id=id)
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def dealerformview(request,id):
    dealer = Dealer.objects.get(id=id)
    dict = {'dealer': dealer}
    return render(request, 'dealer.html', dict)


def dealerformdelete(request, id):
    dealer = Dealer.objects.get(id=id)
    dealer.delete()
    return render(request, 'index.html')


def dealertable(request):
    dealer = Dealer.objects.all()
    dict = {"dealer": dealer}
    return render(request, 'dealertable.html', dict)


def empform(request):
    dict = {'add': True}
    return render(request, 'emp.html', dict)


def empforminsert(request):
    try:
        emp = Employee()
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def empformupdate(request, id):
    try:
        emp = Employee.objects.get(id=id)
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def empformview(request, id):
    emp = Employee.objects.get(id=id)
    dict = {'emp': emp}
    return render(request, 'emp.html', dict)


def empformdelete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return render(request, 'index.html')


def emptable(request):
    emp = Employee.objects.all()
    dict = {"emp": emp}
    return render(request, 'emptable.html', dict)


def custform(request):
    dict = {'add': True}
    return render(request, 'cust.html', dict)


def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def custformupdate(request, id):
    try:
        cust = Customer.objects.get(id=id)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def custformview(request, id):
    cust = Customer.objects.get(id=id)
    dict = {'cust': cust}
    return render(request, 'cust.html', dict)


def custformdelete(request, id):
    cust = Customer.objects.get(id=id)
    cust.delete()
    return render(request, 'index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'custtable.html', dict)


def medform(request):
    dict = {'add': True}
    return render(request, 'med.html', dict)


def medforminsert(request):
    try:
        med = Medicine()
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def medformupdate(request, id):
    try:
        med = Medicine.objects.get(id=id)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def medformview(request, id):
    med = Medicine.objects.get(id=id)
    dict = {'med': med}
    return render(request, 'med.html', dict)


def medformdelete(request, id):
    med = Medicine.objects.get(id=id)
    med.delete()
    return render(request, 'index.html')


def medtable(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'medtable.html', dict)


def purchaseform(request):
    dict = {'add': True}
    return render(request, 'purchase.html', dict)


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def purchaseformupdate(request, id):
    try:
        purchase = Purchase.objects.get(id=id)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "new.html")
    return render(request, 'index.html')


def purchaseformview(request, id):
    purchase = Purchase.objects.get(id=id)
    dict = {'purchase': purchase}
    return render(request, 'purchase.html', dict)


def purchaseformdelete(request, id):
    purchase = Purchase.objects.get(id=id)
    purchase.delete()
    return render(request, 'index.html')


def purchasetable(request):
    purchase = Purchase.objects.all()
    dict = {"purchase": purchase}
    return render(request, 'purchasetable.html', dict)
