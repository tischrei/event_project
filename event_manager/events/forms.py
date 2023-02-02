from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Category, Event
from django.core.exceptions import ValidationError

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
 
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
            "min_group": forms.RadioSelect()
        }
 
        labels = {
            "name": "Was geht ab?",
            "min_group": "Mindestgruppe",
        }
    def clean_sub_title(self) -> str:
        """Das Feld sub_title bereinigen und im Falle
        des Falles einen ValidationError auslösen.
        
        Schema der clean-Methoden: def clean_FELDNAME(self)
        Rückgabe muss der Feldwert sein.
        """
        sub_title = self.cleaned_data["sub_title"]
        sub_title = sub_title.replace("x", "")
        if isinstance(sub_title, str) and "@" in sub_title:
            raise ValidationError("Das @-Symbol ist im Subtitle nicht legal.")


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