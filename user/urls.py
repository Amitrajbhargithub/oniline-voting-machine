from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('contactus/',views.contactus),
    path('uelection/',views.uelection),
    path('result/',views.result),
    path('usignin/',views.usignin),
    path('register/',views.register),
    path('vote/',views.voteforparty),
    path('logout/',views.logout),

]