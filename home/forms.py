from django import forms
from .models import NewProduct


class NewProductForm(forms.ModelForm):
    class Meta:
        model = NewProduct
        fields = ('name', 'category', 'producer', 'photo', 'price')
