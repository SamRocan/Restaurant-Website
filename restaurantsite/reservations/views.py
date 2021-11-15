from django.http import JsonResponse
from django.shortcuts import render
from .models import Reservation, Table
from datetime import datetime, timedelta, timezone
# Create your views here.
def reservations_home(request):
    tables = Table.objects.all()
    reservations = Reservation.objects.all()
    #initialize all tables to not booked
    for table in tables:
        table.booked = False
    start = (reservations.first().date)
    end = (reservations.first().date + timedelta(minutes=100))
    if(request.method=="POST"):
        #initialize all tables to not booked
        for table in tables:
            table.booked = False
        startDate = request.POST.get("dateVar")
        startTime = request.POST.get("timeVar")
        people = int(request.POST.get("numVar"))
        dt = datetime.fromisoformat(startDate + " " + startTime+"+00:00")

        for reservation in reservations:
            tn = reservation.table.table_number
            start = reservation.date - timedelta(minutes=100)
            end = reservation.date + timedelta(minutes=100)
            print(dt)
            print(start)
            print(end)
            if(dt > end or dt < start):
                table = tables.get(table_number=tn)
                table.booked = False
                table.save()
            else:
                table = tables.get(table_number=tn)
                table.booked = True
                table.save()

        tables = Table.objects.all()

        #If no of people is < half capacity of table it can't be booked
        for table in tables:
            if (table.booked == True):
                pass
            elif(table.seats/2 > people):
                table.booked = True
                table.save()
            elif(table.seats < people):
                table.booked = True
                table.save()
            else:
                table.booked = False
                table.save()

    return render(request, 'reservations/reservations_home.html', {'tables':tables, 'reservations':reservations})

def json_view(request):
    result = request.GET.get('result', None)
    print(result)
    data = {
        "worked":"worked",
    }
    return JsonResponse(data)
