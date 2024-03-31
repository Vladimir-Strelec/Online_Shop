from django.core.validators import MinLengthValidator
from django.db import models


class Order(models.Model):
    Min = "120 x 140"
    Mid = "130 x 200"
    Big = "500 x 600"
    ALL_SIZE = [(x, x) for x in (Min, Mid, Big)]

    image = models.ImageField(upload_to='photo/%Y/%m/%d',)
    size = models.CharField(choices=ALL_SIZE, max_length=50, default=Min)
    data_joined = models.DateTimeField(auto_now_add=True, )
    data_edit = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return f"{self.image} -> {self.size} -> {self.data_joined}"


class Address(models.Model):
    Nürnberg = 'Nürnberg'
    Erlangen = 'Erlangen'
    Fürth = 'Fürth'
    Schvabach = 'Schvabach'
    Roth = 'Roth'
    ALL_CITY = [(x, x) for x in (Nürnberg, Erlangen, Fürth, Schvabach, Roth)]

    post_code = models.IntegerField(validators=(MinLengthValidator(5),), unique=False, blank=False)
    city = models.CharField(choices=ALL_CITY, max_length=50, default=Nürnberg)
    street = models.CharField(max_length=50, validators=(MinLengthValidator(2),), unique=False, blank=False)
    house_number = models.CharField(max_length=10, validators=(MinLengthValidator(1),), unique=False, blank=False)
    description = models.CharField(max_length=200,)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE,)


