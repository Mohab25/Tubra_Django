from django.db import models

class Aerodrome(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self)->str:
        return self.Name
