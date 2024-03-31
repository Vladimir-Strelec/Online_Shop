from django import forms

from .models import Order


class CreateOrder(forms.ModelForm, forms.Form):
    class Meta:
        model = Order
        fields = '__all__'

    def is_valid(self):
        if self.data:
            x = self.data
            print(x.values())
            Order.objects.create(image=self.data['image'], size=self.data['size'])
            return True
        return False