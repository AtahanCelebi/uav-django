from django.db import models

# Create your models here.
class IHA(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weight = models.FloatField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.brand + " " + self.model