import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    """Eine Fabrik-Klasse um User zu generieren."""
    class Meta:
        model = get_user_model()

    username = factory.Faker("user_name", locale="de_DE")
    email = factory.Faker("email", locale="de_DE")
    password = factory.LazyFunction(
        lambda: make_password("abc")
    )