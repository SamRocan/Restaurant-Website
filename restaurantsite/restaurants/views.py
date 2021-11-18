from django.shortcuts import render

# Create your views here.
def locations_home(request):
    return render(request, 'restaurants/locations_home.html')