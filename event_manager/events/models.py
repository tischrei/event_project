from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .managers import ActiveManager
from .validators import datetime_in_future

# User-Model immer so importieren aus den Settings zur Portierbarkeit
User = get_user_model()


class DateMixin(models.Model):
    """eine abstrakte Klasse, die selbst keine DB-Tabellen erstellt."""
 
    # setze den aktuellen Zeitstempel einmalig
    created_at = models.DateTimeField(auto_now_add=True)
 
    # setze Zeitstempel immer beim Speichern
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
 
 
class Category(DateMixin):
    """eine Kategorie für den Event, zb. Sport"""

    class Meta:
        ordering = ['name']
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"
 
    # VARCHAR 100
    name = models.CharField(max_length=100)  # per default mandatory (required)
 
    # optionales Feld
    # null => darf NULL sein in der DB,
    # blank => das Formularfeld darf leer sein
    sub_title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.TextField(null=True, blank=True)  # optionales Feld
 
    def __str__(self) -> str:
        """String Repräsentation des Objekts."""
        return self.name
 
 
class Event(DateMixin):
    """ein Event in einer Kategorie"""

    class Group(models.IntegerChoices):
        """basiert intern auf der ENUM-Klasse"""
        BIG = 10, "mittelgroße Gruppe"
        SMALL = 2, "sehr kleiner Gruppe"
        MEDIUM = 5, "kleine Gruppe"
        LARGE = 20, "sehr große Gruppe"
        UNLIMITED = 0, "ohne Limit"

    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100)
        ],
    )
    sub_title = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Checkbox im Formular
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="events"
    )

    date = models.DateTimeField(validators=[datetime_in_future])

    min_group = models.IntegerField(choices=Group.choices)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events"
    )

    # wenn man einen zweiten Manager angibt,  
    # muss objects = models.Manager() definiert werden.
    objects = models.Manager()  # Event.objects.all()
    active_events = ActiveManager()  # Event.active_events.all()
 
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        """
        URL Pfad zum Objekt
        events/event/3
        """
        return reverse("events:event_detail", kwargs={"pk": self.pk})
    
    def related_events(self):
        """
        Return 5 ähnlcihe Objekte zu diesem Geschäftsobjekt
        """
        related_events = Event.objects.filter(
            category=self.category
        )
        return related_events.exclude(pk=self.pk)[:5]
    