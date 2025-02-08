from django.shortcuts import get_object_or_404
from rest_framework import response, status
from rest_framework.views import APIView
from words.models import English, Polish
from words.serializers import EnglishWordSerializer, PolishWordSerializer
from words.serializers import EnglishWordDetailSerializer, PolishWordDetailSerializer

class EnglishWords(APIView):
    def get(self, request):
        words = list(English.objects.all())  # ✅ Performance boost
        serializer = EnglishWordSerializer(words, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class EnglishWordDetail(APIView):
    def get(self, request, word_id):
        word = get_object_or_404(English, id=word_id)
        serializer = EnglishWordDetailSerializer(word)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class PolishWords(APIView):
    def get(self, request):
        words = list(Polish.objects.all())
        serializer = PolishWordSerializer(words, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class PolishWordDetail(APIView):
    def get(self, request, word_id):
        word = get_object_or_404(Polish, id=word_id)
        serializer = PolishWordDetailSerializer(word)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

