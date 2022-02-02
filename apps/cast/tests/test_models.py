from django.test import TestCase
from django.db import IntegrityError

from apps.cast.models import Character, Location, House


class LocationModelTest(TestCase):
    def test_create(self):
        count = Location.objects.count()
        location = Location.objects.create(place="NoneLand")

        self.assertEqual(Location.objects.count(), count+1)
        self.assertTrue(Location.objects.filter(place="NoneLand").exists())
        location.delete()

    def test_unique_place(self):
        place = "NoneLand_1"
        count = Location.objects.count()
        Location.objects.create(place=place)

        self.assertEqual(Location.objects.count(), count+1)

        with self.assertRaises(IntegrityError):
            Location.objects.create(place=place)

    def test_delete_location(self):
        location = Location.objects.create(place="NoneLand")
        count = Location.objects.count()
        location.delete()

        self.assertEqual(Location.objects.count(), count-1)


class HouseModelTest(TestCase):
    def test_create(self):
        count = House.objects.count()
        location = Location.objects.create(place="NoneLand")
        House.objects.create(name="FakeHouse", location=location)

        self.assertEqual(House.objects.count(), count+1)
        self.assertTrue(House.objects.filter(name="FakeHouse").exists())

    def test_delete_house(self):
        location = Location.objects.create(place="NoneLand")
        house = House.objects.create(name="FakeHouse", location=location)
        count = House.objects.count()
        house.delete()

        self.assertEqual(House.objects.count(), count-1)


class CharacterModelTest(TestCase):
    def test_create(self):
        count = Character.objects.count()
        location = Location.objects.create(place="NoneLand")
        house = House.objects.create(name="FakeHouse", location=location)
        Character.objects.create(name="fake_name", lastname="fake_lastname", title="fake_title", house=house,
                                 portrayed_by="fake_actor")

        self.assertEqual(Character.objects.count(), count + 1)
        self.assertTrue(Character.objects.filter(name="fake_name").exists())

    def test_unique_name(self):
        count = Character.objects.count()
        location = Location.objects.create(place="NoneLand")
        house = House.objects.create(name="FakeHouse", location=location)
        Character.objects.create(name="fake_name", lastname="fake_lastname", title="fake_title", house=house,
                                 portrayed_by="fake_actor")

        self.assertEqual(Character.objects.count(), count+1)

        with self.assertRaises(IntegrityError):
            Character.objects.create(name="fake_name", lastname="fake_lastname", title="fake_title", house=house,
                                     portrayed_by="fake_actor")

    def test_delete_character(self):
        location = Location.objects.create(place="NoneLand")
        house = House.objects.create(name="FakeHouse", location=location)
        character = Character.objects.create(name="fake_name", lastname="fake_lastname", title="fake_title", house=house,
                                             portrayed_by="fake_actor")
        count = Character.objects.count()
        character.delete()

        self.assertEqual(Character.objects.count(), count-1)