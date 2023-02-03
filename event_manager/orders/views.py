from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import OrderFormSet, OrderForm
from .models import Order

class OrderCreateView(TemplateView):
    """hier kann ich viele Orders anlegen"""

    template_name = 