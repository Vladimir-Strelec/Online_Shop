from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit
from django import forms

from .models import Painting


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'



