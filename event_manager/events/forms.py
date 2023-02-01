from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Category, Event

# ein zusätzliches Formular ohne ModelForm zu nutzen
# class MyForm(forms.Form):


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit('submit', "Abschicken"))
    
    class Meta:
        model = Event
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    """
    forms.ModelForm => Formular basiert auf
    Category - Model
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class= "col-lg-2"
        self.helper.field_class= "col-lg-8"

        self.helper.add_input(Submit('submit', "Abschicken"))

    class Meta:
        model = Category
        fields = "__all__" # alle Felder nutzen
        # exclude = "name", # Name Feld excludieren
    
    # zusätzliches Feld
    message = forms.CharField(max_length=10, required=False)