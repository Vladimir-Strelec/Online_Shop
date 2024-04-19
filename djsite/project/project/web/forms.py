from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit
from django import forms

from .models import Painting


class PaymentForm(forms.Form):
    image = forms.ImageField()
    size = forms.ChoiceField(choices=Painting.ALL_SIZE)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            "image",
            "size",
            Submit("submit", "Buy", css_class='button white btn-block btn-primary')
        )

