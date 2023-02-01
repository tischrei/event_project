from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    # events/hello
    path("hello", views.hello_world, name="hello_world"),

    # events/categories
    path("categories", views.categories, name="categories"),

    # events/category/3
    path("category/<int:pk>", views.category, name="category_detail"),

    # events/category/add
    path("category/add", views.category_add, name="category_add"),

    # events/category/3/update
    path(
        "category/<int:pk>/update",
        views.category_update,
        name="category_update"
    ),

    # events/event/add
    path(
        "event/add",
        views.EventCreateView.as_view(),
        name="event_add"
    ),
]