from django.test import TestCase
from .models import Menu, MenuSection, MenuItem, ALLERGENS
# Create your tests here.
class MenuTestCase(TestCase):
    def setUp(self):
        starterMenu = Menu.objects.create(name='drinks', information='Lorem Ipsum')
        cocktailSection = MenuSection.objects.create(menu=starterMenu, name='cocktails')
        MenuItem.objects.create(section=cocktailSection,
                                name='Pina Colada',
                                description='Coconut Cocktail',
                                allergens=ALLERGENS[0][4],
                                price=14.99)

    def test_menu(self):
        pinaColada = MenuItem.objects.get(name='Pina Colada')
        self.assertEqual(pinaColada.description, 'Coconut Cocktail')
        self.assertEqual(pinaColada.allergens, ['Milk'])
        self.assertEqual(pinaColada.description, 'Coconut Cocktail')