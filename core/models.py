from django.db import models

class List(models.Model):
    song = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.song