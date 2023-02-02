"""
Zwei Möglichkeiten, Validatoren zu erstellen.
1.) funktionsbasiert(!) a) ohne Parameter, b) mit Parameter
2.) Klasse
"""
from django.core.exceptions import ValidationError
from django.utils import timezone


def datetime_in_future(value) -> None:
    """löst einen ValidationError aus, wenn
    der Zeitpunkt in der Vergangenheit liegt.
    """
    if value < timezone.now():
        raise ValidationError(
            "Der Zeitpunkt darf nicht in der Vergangenheit liegen!"
        )