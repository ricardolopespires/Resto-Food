from django.urls import path
from . import views

app_name = 'management'



urlpatterns = [

    path('manager/', views.Management_View.as_view(), name = 'manager'),

]


