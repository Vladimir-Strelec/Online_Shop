from django import forms

from .models import Order


class CreateOrder(forms.ModelForm, forms.Form):
    class Meta:
        model = Order
        fields = ['image', 'size']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'})
        }

    def is_valid(self):
        if self.data:
            x = self.data
            print(x.values())
            Order.objects.create(image=self.data['image'], size=self.data['size'])
            return True
        return False