from unicodedata import name
from. import views
from django.urls import path,include


urlpatterns = [
    
    path('',views.welcomePage,name='welcome'),
    path('userlogin',views.userLogin,name='userlogin'),
    path('usersignup',views.userSignup,name='usersignup'),
    path('usernameAjax',views.usernameAjax,name='usernameAjax'),
    path('base',views.base,name='base'),
    path('userhome',views.userHome,name='userhome'),
    path('viewquotes',views.viewQuotes,name='viewquotes'),
    path('logout',views.logout,name='logout'),
    path('addquotes',views.addquotes,name='addquotes'),
    path('like',views.Likes,name='like')
]
