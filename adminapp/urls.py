from unicodedata import name
from. import views
from django.urls import path,include


urlpatterns = [
    path('adminsignup',views.Adminsignup,name='adminsignup'),
    path('adminlogin',views.adminLogin,name='adminlogin'),
    path('base',views.base,name='base'),
    path('adminhome',views.adminHome,name='adminhome'),
    path('approvedquotes',views.approvedQuotes,name='approvedquotes'),
    path('Approve',views.Approve,name='Approve'),
    path('Reject/<int:id>',views.Reject,name='Reject'),
    path('adminlogout',views.logout,name='adminlogout'),
]
