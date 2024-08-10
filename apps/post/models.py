from django.db import models

# Create your models here.

class Students(models.Model):
    fullname = models.CharField(
        max_length=155
    )
    age = models.IntegerField(
        default = 0
    )
    hobby = models.TextField(
        
        blank = True, null = True
    )

