from rest_framework import serializers
from words.models import English, Polish


class EnglishWorld(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = [
            'word',
            'description ',
        ]


class PolishWord(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = [
            'word',
            'description'
        ]
