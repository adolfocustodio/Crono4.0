from django import forms
from .models import Postagem


class PostagemForm(forms.ModelForm):
    
    class Meta:
        model = Postagem
        fields = ('titulo', 'desc', 'categoria')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'})
        }
