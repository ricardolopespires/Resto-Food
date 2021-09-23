from django.contrib import admin
from .models import Pizzeria

# Register your models here.




@admin.register(Pizzeria)
class PizzeriaAdmin(admin.ModelAdmin):
    list_display = [ 'pizzeria_name','street','city', 'street', 'email', 'active']
