from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"