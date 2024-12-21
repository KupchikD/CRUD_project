from django.db import models
from django.db.models import CharField, ImageField


# Create your models here.
class Jobs(models.Model):
    image = ImageField(upload_to='images/')
    summary = CharField(max_length=200)

    def __str__(self):
        return self.summary
