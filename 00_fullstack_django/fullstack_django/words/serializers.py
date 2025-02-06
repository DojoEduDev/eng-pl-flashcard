from rest_framework import serializers
from words.models import English, Polish


class EnglishWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = [
            'id',
            'word',
            'description ',
        ]


class PolishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = [
            'id',
            'word',
            'description'
        ]
