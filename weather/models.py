from django.db import models


class Cities(models.Model):
    City = models.CharField('Город', max_length=50)

    def __str__(self):
        return self.City
