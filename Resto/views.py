from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from rest_framework import viewsets
from .serializers import PizzeriaSerializer
from management.models import Pizzeria
from django.http import HttpResponse






class Index_Views(View):

    def get(self,request):
        return render(request, 'initial/index.html')


class PizzeriaViewset(viewsets.ModelViewSet):

    queryset = Pizzeria.objects.all()
    serializer_class =  PizzeriaSerializer


    def get(self, request, format=None):
        return HttpResponse("test")
   


