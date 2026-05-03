from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    #magic method to return the name of the model when we print it
    def __str__(self):
        return self.name
