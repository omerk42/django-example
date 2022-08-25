from django.utils.timezone import now
from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title

