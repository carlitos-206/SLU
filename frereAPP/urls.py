from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('team', views.team, name="team"),
    path('dashboard', views.dashboard),
    path('result', views.result, name="result"),
    path('contact', views.contact, name="contact"),
    path('exit', views.exit, name="exit"),
    ]