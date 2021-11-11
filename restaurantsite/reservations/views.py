from django.shortcuts import render

# Create your views here.
def reservations_home(request):
    return render(request, 'reservations/reservations_home.html')