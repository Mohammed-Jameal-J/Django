from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False)

    def __str__(self):
        return f"{self.id} - {self.name}"
