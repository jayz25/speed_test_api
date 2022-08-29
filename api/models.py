from django.db import models

# Create your models here.
class Paragraph(models.Model):
    paragraph = models.TextField()

class GlobalStats(models.Model):
    user = models.CharField(max_length=20)
    words_per_minute = models.IntegerField()
    characters_per_minute = models.IntegerField()
    accuracy = models.IntegerField()


