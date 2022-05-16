from django.shortcuts import render,redirect

from user.models import AddQuotes, ApproveQuotes
from user.views import userSignup
from .models import *
from user.models import UserSignup
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def Adminsignup(request):
    if request.method=='POST':
        userName=request.POST['username']
        password=request.POST['password']
        adminData=AdminSignup(userName=userName,password=password)
        adminData.save()
    return render(request,'adminsignup.html')


def adminLogin(request):
    if request.method=='POST':
        userName=request.POST['adminname']
        password=request.POST['password']
        uservalidate=AdminSignup.objects.get(userName=userName)
        if uservalidate.userName==userName and uservalidate.password==password:
            request.session['admin_session']=uservalidate.id
            return redirect('adminhome')
        return redirect('adminlogin')    
    return render(request,'adminlogin.html')

def base(request):
    return render(request,'base.html')


def adminHome(request):
    quotes=AddQuotes.objects.select_related("userName").order_by('-id')
    return render(request,'adminhome.html',{'quotes':quotes})

def approvedQuotes(request):
    appproved=ApproveQuotes.objects.all().order_by('-id')
    return render(request,'approvedQuotes.html',{'appproved':appproved})


@csrf_exempt
def Approve(request):
    user_id=UserSignup.objects.get(id=request.session['user_session'])
    if request.method=='POST':
        Quotes_id=AddQuotes.objects.get(id=request.POST['quotes_id'])
        Approvequotes=ApproveQuotes(user=user_id,quotes=Quotes_id)
        Approvequotes.save()
        return JsonResponse({"message":"Post Approved"}) 
    return redirect('approvedquotes')




def Reject(request,id):
    AddQuotes.objects.filter(id=id).delete()
    return redirect('adminhome')        



def logout(request):
    try:
        request.session.flush()
        return redirect('adminlogin')
    except AdminSignup.DoesNotExist:
        return render(request,'adminlogin.html')        

        