from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from user.factories import UserFactory

class Command(BaseCommand):
    """
    eigene Subcommands erben immer von BaseCommand
    """

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            help="Number of Users to be generated",
            required=True)
        
        parser.epilog = "Usage: python manage.py create_user -n 20"

    def handle(self, *args, **kwargs):
        print("Mein erstes Subkommando!")
        n = kwargs.get("number")
        print("number of users:", kwargs.get("number"))

        user_list = get_user_model().objects.exclude(username="admin").delete()
        UserFactory.create_batch(n)
        print("Successfully created")
