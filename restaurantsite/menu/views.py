from django.shortcuts import render
from .models import Menu, MenuSection, MenuItem
# Create your views here.
def menu_home(request):

    menu = Menu.objects.all()
    return render(request, 'menu/menu_home.html', {'menu':menu})