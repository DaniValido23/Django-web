from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from services.models import Service, Order

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        total = self.request.session['total']

        super().__init__(*args, **kwargs)

        self.fields['total'].initial = total

    class Meta:
        model = Order
        fields = ['name', 'address', 'colonia', 'email', 'total']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),
            'colonia': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Colonia'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'total': TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            })
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título',
            }),
            'subtitle': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtítulo',
            })
        }

    # Validation function
    def clean(self):
        super(ServiceForm, self).clean()

        title = self.cleaned_data['title']

        if len(title) < 5:
            self.errors['title'] = self.error_class(['Mínimo 5 caracteres'])

        return self.cleaned_data
