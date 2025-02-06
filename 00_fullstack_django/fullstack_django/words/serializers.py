from rest_framework import serializers
from words.models import English, Polish


class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = [
            'id',
            'word',
        ]

class EnglishWordDetialSeralizer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = [
            'id',
            'word',
            'description '
        ]

class PolishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = [
            'id',
            'word',
        ]

class PolishWordDetialSeralizer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = [
            'id',
            'word',
            'description '
        ]
