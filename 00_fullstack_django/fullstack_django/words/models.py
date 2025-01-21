from django.db import models

class Polish(models.Model):
    word = models.TextField()
    desciption = models.TextField()

class English(models.Model):
    world = models.TextField()
    description = models.TextField()

    polish = models.ForeignKey(to=Polish, on_delete=models.CASCADE)
