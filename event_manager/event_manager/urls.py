from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("events/", include("events.urls")),
    path("", RedirectView.as_view(url="events/")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
