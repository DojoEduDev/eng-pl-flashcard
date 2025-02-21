from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from words.models import English, Polish
from words.serializers import EnglishWordSerializer, PolishWordSerializer
from words.serializers import EnglishWordDetailSerializer, PolishWordDetailSerializer


@extend_schema(tags=["English Words"])
class EnglishWords(APIView):
    @extend_schema(
        summary="Retrive all English words.",
        description="Returns a list of all English words with their IDs.",
        responses={
            200: EnglishWordSerializer(many=True),
        },
    )
    def get(self, request: Request):
        words = list(English.objects.all())
        serializer = EnglishWordSerializer(words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        summary="Create a new English word.",
        description="Creates a new English `word` with `discription`.",
        request=EnglishWordDetailSerializer,
        responses={
            201: EnglishWordDetailSerializer(),
            400: "Incorrect JSON",
        }
    )
    def post(self, request: Request):
        serializer = EnglishWordDetailSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        english_word, created = English.objects.get_or_create(
            word=serializer.validated_data["word"],
            defaults={"description": serializer.validated_data["description"]}
        )

        return Response(EnglishWordDetailSerializer(english_word).data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["English Words"])
class EnglishWordDetail(APIView):
    @extend_schema(
        summary="Retrive an word based on id.",
        description="Returns the `English` `word` based on `ID`.",
        responses={
            200: EnglishWordDetailSerializer(),
            404: None,
        },
    )
    def get(self, request: Request, word_id: int):
        word = get_object_or_404(English, id=word_id)
        serializer = EnglishWordDetailSerializer(word)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Delete a word based on `ID`.",
        description="Delete a `English` word based on `ID`.",
        responses={
            200: "",
            404: None,
        },
    )
    def delete(self, request: Request, word_id: int):
        word: Polish = get_object_or_404(English, id=word_id)
        word.delete()
        return Response(status=status.HTTP_200_OK)


@extend_schema(tags=["Polish Words"])
class PolishWords(APIView):
    @extend_schema(
        summary="Retrieve all Polish words.",
        description="Returns a list of all Polish words with their IDs.",
        responses={200: PolishWordSerializer(many=True)},
    )
    def get(self, request: Request):
        words = Polish.objects.all()
        serializer = PolishWordSerializer(words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create a new Polish word.",
        description="Creates a new Polish `word` with `description` if it does not already exist.",
        request=PolishWordDetailSerializer(),
        responses={
            201: PolishWordDetailSerializer(),
            400: "Incorrect JSON",
        }
    )
    def post(self, request: Request):
        serializer = PolishWordDetailSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        polish_word, created = Polish.objects.get_or_create(
            word=serializer.validated_data["word"],
            defaults={"description": serializer.validated_data["description"]}
        )

        return Response(
            PolishWordDetailSerializer(polish_word).data, status=status.HTTP_201_CREATED
        )


@extend_schema(tags=["Polish Words"])
class PolishWordDetail(APIView):
    @extend_schema(
        summary="Retrives a word based on `ID`.",
        description="Returns `Polish` word based on `ID`.",
        responses={
            200: PolishWordDetailSerializer(),
            404: None,
        },
    )
    def get(self, request: Request, word_id: int):
        word = get_object_or_404(Polish, id=word_id)
        serializer = PolishWordDetailSerializer(word)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        summary="Delete a word based on `ID`.",
        description="Delete a `Polish` word based on `ID`.",
        responses={
            200: "",
            404: None,
        },
    )
    def delete(self, request: Request, word_id: int):
        word: Polish = get_object_or_404(Polish, id=word_id)
        word.delete()
        return Response(status=status.HTTP_200_OK)
