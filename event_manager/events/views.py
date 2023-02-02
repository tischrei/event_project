from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Category, Event
from .forms import CategoryForm, EventForm


class EventDeleteView(LoginRequiredMixin, DeleteView):
    """
    event/3/delete
    Template name: event_confirm_delete.html
    """
    model = Event
    success_url = reverse_lazy("events:events")


class ActiveEventListView(ListView):
    """zeige hier nur aktive Events an
    dazu überschreiben wir das QS.
    events/active
    """
    model = Event
    queryset = Event.active_events.all()


class EventSearchView(ListView):
    """ 
    http://127.0.0.1:8000/events/search?q=suchwort
    """
    model = Event
 
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "")
        
        return qs.filter(Q(name__icontains=q) | Q(sub_title__icontains=q))
    

class EventListView(ListView):
    """ 
    http://127.0.0.1:8000/events
    Template Name ist: MODELNAME_list.html
    """
    model = Event
    # prefetch_related: alle related Objekte vorladen. Reduziert Datenbank - Hits
    queryset = Event.objects.prefetch_related("category", "author").all()
 
 
class EventDetailView(DetailView):
    """
    http://127.0.0.1:8000/events/event/3
    Template Name ist: MODELNAME_detail.html
    """
    model = Event


class EventCreateView(CreateView):
    """
    das Default-Template einer CreateView ist _form.html
    events/event/add
    """
    model = Event
    form_class = EventForm

def category_add(request: HttpRequest) -> HttpResponse:
    """
    trage eine neue Kategorie ein (stell Form zur Verfügung und
    sepichert in DB)
    events/categoriy/add
    """
    if request.method == "POST":
        # test
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # im Erfolgsfall machen wir einen redirect auf Kategorie-Seite
            return redirect("events:categories")
    else:
        # leeres Formular zurückgeben
        form = CategoryForm()
    
    return render(request, "events/category_add.html", {
        "form": form
    })
    
def category_update(request: HttpRequest, pk: int) -> HttpResponse:
    """
    eine Kategorie updaten
    events/categorie/3/update
    """
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect("events:categories")
    
    return render(request, "events/category_add.html", {
        "form": form
    })



def category(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Aufruf einer Kategorie Detailseite
    """
    category = get_object_or_404(Category, pk=pk)

    return render(request, "events/category.html", {
        "category": category
    })

def categories(request: HttpRequest) -> HttpResponse:
    """
    events/categories
    """
    categories = Category.objects.all()
    context_dict = {
        "categories": categories
    }
    return render(request, "events/categories.html", context_dict)


def hello_world(request: HttpRequest) -> HttpResponse:
    
    print("Request Object:", request)
    print("Request Method:", request.method)
    print("Request User:", request.user)
    return HttpResponse("hello world")