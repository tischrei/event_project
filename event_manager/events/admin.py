from django.contrib import admin
from .models import Category, Event


# einfachste Möglichkeit, ein Model in der Admin zu registrieren
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sub_title", "number_of_events"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "sub_title", "description"]

    def number_of_events(self, obj):
        return obj.events.count()