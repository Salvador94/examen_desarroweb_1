from django import forms

from .models import Libro

class LibroModelForm(forms.ModelForm):
    # content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':"Tweet",'class': "textarea"}))

    class Meta:
        model = Libro
        fields = [
            #"user",
            "Nombre",
            "Autor",
            "ISBN",
            "Editorial",
            "precio",
            ]
