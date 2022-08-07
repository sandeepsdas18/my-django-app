from django.db import models

# Create your models here.

class Input(models.Model):
    input_text = models.CharField(max_length=250)
    country_name = models.CharField(max_length=250)