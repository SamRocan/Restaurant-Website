from django.http import JsonResponse
from django.shortcuts import render
from .models import Reservation, Table
# Create your views here.
def reservations_home(request):
    tables = Table.objects.all()
    return render(request, 'reservations/reservations_home.html', {'tables':tables})

def json_view(request):
    result = request.GET.get('result', None)
    print(result)
    data = {
        "worked":"worked",
    }
    return JsonResponse(data)
