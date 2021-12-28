from django.urls import path
from . import views 

urlpatterns=[
    #LOGIN VERIFICATION
    path('',views.index,name='index'),
    path('team', views.team, name="team"),
    
    #TRANSLATION TOOL
    path('dashboard', views.dashboard),
    path('result', views.result, name="result"),
    
    #SIDEBAR MENU 
    path('contact', views.contact, name="contact"),
    path('schedule', views.schedule, name="schedule"),
    path('safety', views.safety, name="safety"),
    
    #LOGOUT
    path('exit', views.exit, name="exit"),
    ]