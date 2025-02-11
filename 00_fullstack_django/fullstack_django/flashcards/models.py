from django.db import models

from words.models import English, Polish


class FlashCard(models.Model):
    english_word = models.ForeignKey(English, on_delete=models.CASCADE)
    polish_word = models.ForeignKey(Polish, on_delete=models.CASCADE)
