from django.db import models

from words.models import English, Polish


class FlashCard(models.Model):
    """
    FlashCard model that connects an English word with its Polish equivalent.
    
    Fields:
        english_word (ForeignKey): Reference to an English word.
            If deleted, associated flashcards are also removed.
        polish_word (ForeignKey): Reference to a Polish word.
            If deleted, associated flashcards are also removed.
    """

    english_word = models.ForeignKey(English, on_delete=models.CASCADE, related_name="flashcards")
    polish_word = models.ForeignKey(Polish, on_delete=models.CASCADE, related_name="flashcards")

    def __str__(self):
        return f"{self.english_word.word} - {self.polish_word.word}"
