from django import forms
from .models import Person
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput, CheckboxInput


class RideForm(forms.Form):
    origination_city = forms.CharField(label='Origination City', max_length=64, required=False)
    origination_state = forms.CharField(label='Origination State', max_length=2, required=False)
    destination_city = forms.CharField(label='Destination City', max_length=64, required=False)
    destination_state = forms.CharField(label='Destination State', max_length=2, required=False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []
    widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'age': NumberInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'name@example.com', 'class': 'form-control'}),
            'origination_city': TextInput(attrs={'placeholder': 'City of departure', 'class': 'form-control'}),
            'origination_state': TextInput(attrs={'placeholder': 'State of departure (e.g., NJ)', 'class': 'form-control'}),
            'destination_city': TextInput(attrs={'placeholder': 'Destination city', 'class': 'form-control'}),
            'destination_state': TextInput(attrs={'placeholder': 'Destination state (e.g., NY)', 'class': 'form-control'}),
            'vehicle_make': TextInput(attrs={'placeholder': 'Make of the vehicle', 'class': 'form-control'}),
            'vehicle_model': TextInput(attrs={'placeholder': 'Model of the vehicle', 'class': 'form-control'}),
            'vehicle_color': TextInput(attrs={'placeholder': 'Color of the vehicle', 'class': 'form-control'}),
            'date': DateInput(attrs={'placeholder': 'MM/DD/YYYY', 'class': 'form-control'}),
            'time': TextInput(attrs={'placeholder': 'HH:MM', 'class': 'form-control'}),
            'is_regular': CheckboxInput(attrs={'class': 'form-check-input'}),
            'taking_passengers': CheckboxInput(attrs={'class': 'form-check-input'}),
            'seats_available': NumberInput(attrs={'class': 'form-control', 'value': 1}),
        }
