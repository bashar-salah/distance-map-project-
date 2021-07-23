from django.db import models

# Create your models here.
class map (models.Model) :
    destnation  = models.CharField(max_length=100)
    distance = models.FloatField()
    myplace = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.destnation