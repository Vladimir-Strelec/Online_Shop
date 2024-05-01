from django.db import models


class Painting(models.Model):
    MIN = "160 X 230"
    NORMAL = "260 X 330"
    BIG = "1160 X 930"
    ALL_SIZE = [(x, x) for x in (MIN, NORMAL, BIG)]

    image = models.ImageField(upload_to='images/',)
    size = models.CharField(choices=ALL_SIZE, default=MIN, max_length=100)
    paid = models.BooleanField(default=False,)
    status = models.BooleanField(default=False,)

    def __str__(self):
        return f"{self.image} - {self.size} - {self.paid} - {self.status}"