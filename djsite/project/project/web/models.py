from django.db import models


class Painting(models.Model):
    MIN = "160 X 230"
    NORMAL = "260 X 330"
    BIG = "1160 X 930"
    ALL_SIZE = [(x, x) for x in (MIN, NORMAL, BIG)]

    image = models.ImageField()
    size = models.CharField(choices=ALL_SIZE, default=MIN, max_length=100)
    paid = models.BooleanField(blank=False, null=False)
    status = models.BooleanField(blank=False, null=False)
