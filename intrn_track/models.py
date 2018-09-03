from django.db import models
from django.utils import timezone

class Card(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    status=models.CharField(max_length=100)
    section=models.IntegerField(default=1)
    create_date=models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title