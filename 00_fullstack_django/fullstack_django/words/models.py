from django.db import models


class English(models.Model):
    """
    Model for English words.
    
    Fields:
        word (CharField) - The English word.
        description (TextField) - A brief definition.
    """
    word = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.word.capitalize()} - {self.description}."


class Polish(models.Model):
    """
    Model for Polish words.
    
    Fields:
        word (CharField) - The Polish word.
        description (TextField) - A brief definition.
    """
    word = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.word.capitalize()} - {self.description}."
 