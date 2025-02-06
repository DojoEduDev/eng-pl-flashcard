from django.db import models


class English(models.Model):
    word = models.TextField()
    description = models.TextField()


class Polish(models.Model):
    word = models.TextField()
    description = models.TextField()
 

class FlashCard(models.Model):
    english = models.ForeignKey(English, on_delete=models.CASCADE)
    polish = models.ForeignKey(Polish, on_delete=models.CASCADE)
