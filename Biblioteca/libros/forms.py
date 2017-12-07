from django import forms

from .models import Libro

class LibroModelForm(forms.ModelForm):
    # content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':"Tweet",'class': "textarea"}))
    Nombre      = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Nombre del libro", 'size': '30'}))
    Autor       = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Autor del libro", 'size': '30'}))
    Editorial   = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Editorial de imprenta",'size': '30'}))
    ISBN        = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"ISBN",'size': '30'}))
    precio      = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':"Precio"}))


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
