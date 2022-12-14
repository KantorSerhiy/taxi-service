from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


# Create your tests here.


class ModelTest(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test name", country="test country"
        )

        self.assertEqual(str(manufacturer), "test name test country")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="test username",
            password="test1234",
            first_name="test first",
            last_name="test last",
        )

        self.assertEqual(
            str(driver),
            f"{driver.username} " f"({driver.first_name} {driver.last_name})",
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test name", country="test country"
        )
        car = Car.objects.create(
            model="test model",
            manufacturer=manufacturer,
        )

        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license(self):
        username = "test"
        password = "test12345"
        license_number = "OIN45698"
        driver = get_user_model().objects.create_user(
            username=username, password=password, license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)
