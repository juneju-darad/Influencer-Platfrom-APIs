from django.urls import path
from . import views

urlpatterns = [
    path('', views.ythome, name='ythome'),
    path('ytresult', views.ytresult, name='ytresult')
]