from rest_framework import serializers

from flashcards.models import FlashCard
from words.serializers import EnglishWordDetailSerializer, PolishWordDetailSerializer
from words.models import English, Polish

class FlashCardSerializer(serializers.ModelSerializer):
    """
    Flashcard Serializer: Connects English and Polish words.
    
    - Uses detailed nested serializers for reading.
    - Uses `PrimaryKeyRelatedField` for writing.
    """

    english_word = EnglishWordDetailSerializer(read_only=True)
    polish_word = PolishWordDetailSerializer(read_only=True)

    english_word_id = serializers.PrimaryKeyRelatedField(
        queryset=English.objects.all(), write_only=True
    )
    polish_word_id = serializers.PrimaryKeyRelatedField(
        queryset=Polish.objects.all(), write_only=True
    )

    class Meta:
        model = FlashCard
        fields = [
            'id',
            'english_word',
            'polish_word',
            'english_word_id',
            'polish_word_id'
        ]

class RequestFullFlashCardSerializer(serializers.Serializer):
    english_word = EnglishWordDetailSerializer()
    polish_word = PolishWordDetailSerializer()
