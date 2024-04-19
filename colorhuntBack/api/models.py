from django.db import models

# Create your models here.
class Palette(models.Model):
    likes = models.IntegerField()
    color1 = models.CharField(max_length=7)
    color2 = models.CharField(max_length=7)
    color3 = models.CharField(max_length=7)
    color4 = models.CharField(max_length=7)
    
    def __str__(self) -> str:
        return str(self.id) 
    