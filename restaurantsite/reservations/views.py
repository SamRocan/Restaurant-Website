from django.http import JsonResponse
from django.shortcuts import render
from .models import Reservation, Table
from .forms import ReservationForm
from datetime import datetime, timedelta, timezone
# Create your views here.
def reservations_home(request):
    tables = Table.objects.all()
    reservations = Reservation.objects.all()
    request.session['reservation'] = []
    #initialize all tables to not booked
    for table in tables:
        table.booked = False
        table.save()

    if(request.method=="POST"):
        #initialize all tables to not booked
        for table in tables:
            table.booked = False
            table.save()
        startDate = request.POST.get("dateVar")
        startTime = request.POST.get("timeVar")
        people = int(request.POST.get("numVar"))
        request.session['reservation'] = [startDate, startTime, people]
        dt = datetime.fromisoformat(startDate + " " + startTime+"+00:00")

        tables = Table.objects.all()

        #If no of people is < half capacity of table it can't be booked
        for table in tables:
            #print(str(table.table_number) + " " + str(table.booked))

            if(table.seats/2 > people):
                table.booked = True
                table.save()
            elif(table.seats < people):
                table.booked = True
                table.save()
            else:
                table.booked = False
                table.save()


        for reservation in reservations:
            tn = reservation.table.table_number
            start = reservation.date - timedelta(minutes=100)
            end = reservation.date + timedelta(minutes=100)
            if(dt < end and dt > start):
                for table in tables:
                    if (tn == table.table_number):
                        table.booked = True
    return render(request, 'reservations/reservations_home.html', {'tables':tables, 'reservations':reservations})

def reservation_confirm(request):

    info = request.session['reservation']
    for i in info:
        print(i)

    t = str(request.session['table']).replace('Table_', '')
    table = Table.objects.get(table_number=int(t))
    dt = datetime.fromisoformat(str(info[0]) + " " + str(info[1]) +"+00:00")
    info.append(request.session['table'])
    form = ReservationForm
    if request.method == 'POST':
        form = ReservationForm(request.POST)
            # check whether it's valid:
        if form.is_valid():
            email = form.email
            name = form.name
            Reservation.objects.create(table=table, name=name, email=email,  people=info[2], date=dt)
            return render('main/index.html')

    return render(request, 'reservations/reservation_confirm.html', {'info':info, 'form':form})

def reservation_complete(request):
    info = request.session['reservation']
    for i in info:
        print(i)

    t = str(request.session['table']).replace('Table_', '')
    table = Table.objects.get(table_number=int(t))
    dt = datetime.fromisoformat(str(info[0]) + " " + str(info[1]) +"+00:00")
    info.append(request.session['table'])
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            Reservation.objects.create(table=table, name=name, email=email,  people=info[2], date=dt)
            return render(request,'main/index.html')

def json_view(request):
    request.session['table'] = request.GET.get('result', None)
    data = {
        "info":request.session['reservation'],
    }
    return JsonResponse(data)