from re import T
from statistics import mode
from django.db import models
from base.models import BaseModel, BaseManager


# Create your models here.
class Car(BaseModel):
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    COLOR = (
      (0, 'RED'),
      (1, 'BLUE'),
    )

    car = models.CharField(max_length=255, verbose_name="Car Name", unique=True)
    color = models.BooleanField(choices=COLOR, default=0)
    front_of = models.ForeignKey(to='cars.Car', on_delete=models.CASCADE,
                                 related_name="front_of_car", blank=True,
                                 null=True)

    objects = BaseManager()

    def __str__(self):
        return f"{self.car}"

