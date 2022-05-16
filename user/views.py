
from cgi import FieldStorage
from fileinput import filename
from logging import exception
from random import random
from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse

# Create your views here.

#landing page
def welcomePage(request):
    return render(request,'welcomepage.html')


#userlogin page
def userLogin(request):
    if request.method=='POST':
        userName=request.POST['username']
        password=request.POST['password']
        uservalidate=UserSignup.objects.get(userName=userName)
        if uservalidate.userName==userName and uservalidate.password==password:
            request.session['user_session']=uservalidate.id
            return redirect('userhome')
        return redirect('userlogin')    
    return render(request,'userlogin.html')


#user Signup page
def userSignup(request):
    if request.method=='POST':
        name=request.POST['name']
        userName=request.POST['username']
        password=request.POST['password']
        userData=UserSignup(name=name,userName=userName,password=password)
        userData.save()
        
    return render(request,'usersignup.html')   

# check username ..username already exist
def usernameAjax(request):
    uname=request.POST['username']
    try:
        UserSignup.objects.get(name=uname)
        return JsonResponse({'message':True})

    except:
        return JsonResponse({'message':False})     


#basepage 
def base(request):
    return render(request,'basepage.html')

#user home page
def userHome(request):
    return render(request,'userhome.html')  


#view quotes      
def viewQuotes(request):
    quotes=ApproveQuotes.objects.all().order_by('-id')
    return render(request,'viewQuotes.html',{'quotes':quotes})





def logout(request):
    try:
        request.session.flush()
        return redirect('userlogin')
    except UserSignup.DoesNotExist:
        return render(request,'userlogin.html')



def addquotes(request):
    if request.method=='POST':
            quotes=request.POST['quotes']

            user=request.session['user_session']
           
            userquotes=AddQuotes(quotes=quotes,userName_id=user)
            userquotes.save()
    return render(request,'addquotes.html')        

def Like(request):
    pass
    return redirect('userhome')    