from django.db import models
from django.contrib.auth.models import User # allows me to access super user Maria
import datetime

# Create your models here.
class Post(models.Model):
    date = models.DateField(default=datetime.date.today)
    description = models.TextField(blank = True)
    title = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank = True)
    body = models.TextField(blank = True)
    scamType = models.CharField(max_length=255, choices=[('Link','Phishing with a link'), ('Reply', 'Reply to')])
    link = models.CharField(max_length=255, blank = True)
    notes = models.TextField(blank = True)
    #image = models.ImageField(blank = True)

    def __str__(self):
        return self.title
