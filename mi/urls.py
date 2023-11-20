from mi.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumra/',bumra,name='bumra'),
]