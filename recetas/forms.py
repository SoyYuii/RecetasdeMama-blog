from django import forms
from .models import Receta


class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta

        fields = [
            'titulo',
            'descripcion',
            'ingredientes',
            'preparacion',
            'imagen',
            'categoria'
        ]

        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'descripcion': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'ingredientes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 6}
            ),
            'preparacion': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 8}
            ),
            'imagen': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
            'categoria': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }