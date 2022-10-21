from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import DriverCreationForm, validate_license_number


class DriverFormTest(TestCase):
    def test_driver_creation_form_with_license_number_is_valid(self):
        form_data = {
            "username": "test",
            "password1": "Qwer123456",
            "password2": "Qwer123456",
            "first_name": "test first name",
            "last_name": "test last name",
            "license_number": "QWE12345"
        }

        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_validate_license_number(self):
        license_number = "QWE12345"
        self.assertTrue(validate_license_number(license_number))


class PrivateDriverTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test", "Qwer123456"
        )
        self.client.force_login(self.user)

    def test_create_drivers(self):
        form_data = {
            "username": "test",
            "password1": "Qwer123456",
            "password2": "Qwer123456",
            "first_name": "test first name",
            "last_name": "test last name",
            "license_number": "QWE12345"
        }

        self.client.post(reverse("taxi:driver-create"), date=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.username, form_data["username"])
