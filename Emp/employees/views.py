from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee

def insert(request):
    return render(request,'insert.html')

def tosave(request):
    empno1 = request.GET.get('empno')
    empname1 = request.GET.get('empname')
    password1 = request.GET.get('password')

    request.session['name'] = empname1
    ename=request.session['name']

    data = Employee(empno=empno1, empname=empname1, password=password1)
    data.save()
    return render(request,'welcome.html', {'ename':ename})

def index(request):
    data=Employee.objects.all()
    return render(request,'index.html', {'data':data})

def slider(request):
    return render(request,'slider.html')