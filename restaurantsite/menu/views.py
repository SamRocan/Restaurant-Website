from django.shortcuts import render, get_object_or_404
from .models import Menu, MenuSection, MenuItem
# Create your views here.
def menu_home(request):
    menu = Menu.objects.all()
    return render(request, 'menu/menu_home.html', {'menu':menu})

def menu(request, slug):
    menu_cat = get_object_or_404(Menu, slug=slug)
    context = {'menu_cat':menu_cat}
    return render(request,"menu/menu.html",context)

