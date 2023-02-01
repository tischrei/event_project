from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def hello_world(request: HttpRequest) -> HttpResponse:
    
    print("Request Object:", request)
    print("Request Method:", request.method)
    print("Request User:", request.user)
    return HttpResponse("hello world")