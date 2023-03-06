from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http.response import HttpResponse
from django.contrib import messages
from  . models import Registration,Course

# Create your views here.
def index(request):
    return render(request, 'index.html')


def courses(request):
    data=Course.objects.all()
    return render(request,'courses.html',{"data":data})


def dashboard(request):
    return render(request, 'dashboard.html')


def employees(request):
    return render(request, 'employees.html')


def notifications(request):
    return render(request, 'notifications.html')


def pgdashboard(request):
    return render(request, 'pg_dashboard.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'sign-up.html')


def tables(request):
    return render(request, 'tables.html')


def tenants(request):
    return render(request, 'tenants.html')


def viewstudents(request):
    return render(request , 'viewstudents.html')

#registration 
def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(email=email).exists():
            messages.error(request, "email already exists")
            return redirect('/')
        elif Registration.objects.filter(contact=contact).exists():
            messages.error(request, "contact number already exists")
            return redirect('/')
        else:
            Registration.objects.create(name=name,email=email,password=password , contact=contact)
            return redirect('/')
        
        
#login
def login(request):
    if request.method =="POST":
        contact = request.POST['contact']
        password = request.POST['password']
        if Registration.objects.filter(contact=contact).exists():
            inst = Registration.objects.get(contact=contact)
            psw = inst.password
            if check_password(password,psw):
                return redirect('/dashboard/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse("phone number is not registered") 
        
        
#add course


def addcourse(request):
    if request.method=='POST':
        name=request.POST['course']
        fees=request.POST['fees']
        duration=request.POST['duration']
        comments=request.POST['comment']
        if Course.objects.filter(name=name).exists():
            messages.error(request, "already exists")
            data=Course.objects.all()
            return render(request,'courses.html',{'data':data})
        else:
            Course.objects.create(name=name,fees=fees,duration=duration,comments=comments)
            data=Course.objects.all()
            return render(request,'courses.html',{'data':data})
    else:
        return render(request,'courses.html',{'data':data})
    

#delete course

def delete(request , pk):
    use = Course.objects.filter(id=pk).delete()
    return redirect('/courses/')
        



    
            
            
        
        
               
               
             