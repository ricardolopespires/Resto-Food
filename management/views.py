
from django.views.generic import  View
from django.shortcuts import render
from .models import Pizzeria
from rest_framework import viewsets




# Create your views here.



class Management_View(View):

    def get(self, request):
        return render(request, 'management/manager.html')






