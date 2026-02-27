from django import forms
from . import models


class InflowForm(forms.ModelForm):
    class Meta:
        model = models.Inflow
        fields = ['product', 'supplier', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'supplier': 'Fornecedor',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }