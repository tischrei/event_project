from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    # events/hello
    path("hello", views.hello_world, name="hello_world"),

    # events/categories
    path("categories", views.categories, name="categories"),
]