
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

    if 'user_session' in request.session:
        return redirect('userhome')

    if request.method=='POST':
        userName=request.POST['username']
        password=request.POST['password']
        try:
            uservalidate=UserSignup.objects.get(userName=userName)
            if uservalidate.userName==userName and uservalidate.password==password:
                request.session['user_session']=uservalidate.id
                return redirect('userhome')
            else:
                return render(request,'userlogin.html',{'message':'Login Failed','message2':'Incorrect Your Password'})
        except:
            return render(request,'userlogin.html',{'message':'Login Failed','message2':'Incorrect Your username'})    
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




#logout 
def logout(request):
    try:
        request.session.flush()
        return redirect('userlogin')
    except UserSignup.DoesNotExist:
        return render(request,'userlogin.html')


#add quotes page
def addquotes(request):
    if request.method=='POST':
            quotes=request.POST['quotes']

            user=request.session['user_session']
           
            userquotes=AddQuotes(quotes=quotes,userName_id=user)
            userquotes.save()
            return redirect('viewquotes')
    return render(request,'addquotes.html')        



#like function
def Likes(request):

    if request.method=='POST':
        temp = request.POST['li_post']
        post=ApproveQuotes.objects.get(id=temp)

        if 'like' in request.POST:
            user = request.session['user_session']
           
            post.like_counts+=1
            post.save()
            obj = Like(like_user_id=user,post_key_id=temp)
            obj.save()

        if 'unlike' in request.POST:
            temp = request.POST['li_post']
            user = request.session['user_session']
            obj2 = Like.objects.get(like_user_id=user,post_key=temp)
            obj2.delete()
            post.like_counts-=1
            post.save()
            
    return redirect('viewquotes')