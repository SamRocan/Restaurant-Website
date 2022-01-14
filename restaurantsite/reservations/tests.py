from django.test import TestCase
from .models import Reservation, Table
from datetime import datetime
# Create your tests here.
class ReservationsTestCase(TestCase):
    def setUp(self):
        table_1 = Table.objects.create(
            table_number=1,
            seats=5,
            booked=False,
            svg_path=""
        )
        table_2 = Table.objects.create(
            table_number=2,
            seats=2,
            booked=True,
            svg_path=""
        )
        table_3 = Table.objects.create(
            table_number=5,
            seats=8,
            booked=False,
            svg_path=""
        )
        Reservation.objects.create(
            table=table_1,
            name='John Doe',
            people=3,
            email='JDoe@gmail.com',
            date= datetime.now()
        )
        Reservation.objects.create(
            table=table_3,
            name='Random Person',
            people=7,
            email='RPersom493@gmail.com',
            date= datetime(2022, 2, 20)
        )
        Reservation.objects.create(
            table=table_2,
            name='Sam Clendenan',
            people=2,
            email='samclendenan@icloud.com',
            date=datetime(2022, 4, 5)
        )

    def test_table(self):
        t1 = Table.objects.get(table_number=1)
        self.assertEqual(t1.seats, 5)

        t2 = Table.objects.get(table_number=2)
        self.assertEqual(t2.booked, True)

        t3 = Table.objects.get(table_number=5)
        self.assertEqual(t3.table_number, 5)


    def test_reservation(self):
        r1 = Reservation.objects.get(id=1)
        self.assertEqual(table=5)

        r2 = Reservation.objects.get(id=2)
        self.assertEqual(email='RPersom493@gmail.com')

        r3 = Reservation.objects.get(id=2)
        self.assertEqual(name='Sam Clendenan')