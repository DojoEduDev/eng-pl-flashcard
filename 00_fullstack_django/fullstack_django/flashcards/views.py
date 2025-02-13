from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
import logging

from flashcards.models import FlashCard
from flashcards.serializers import FlashCardSerializer, RequestFullFlashCardSerializer
from words.models import English, Polish

logger = logging.getLogger(__name__)


@extend_schema(tags=["FlashCards"])
class FlashCardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage `FlashCards` using existing `English` and `Polish` words.
    """
    
    @extend_schema(
        summary="Retrieves all Flashcards.",
        description="Return a list of all Eng-Pol flashcards.",
        responses={200: FlashCardSerializer(many=True)},
    )
    def list(self, request):
        queryset = FlashCard.objects.all()
        serializer = FlashCardSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Retrieves a Flashcard.",
        description="Return a `Flashcard` based on provided `ID`.",
        responses={200: FlashCardSerializer(), 404: None},
    )
    def retrieve(self, request, pk):
        flashcard = get_object_or_404(FlashCard, pk=pk)
        serializer = FlashCardSerializer(flashcard)
        return Response(serializer.data)

    @extend_schema(
        summary="Creates a Flashcard.",
        description="Create a `Flashcard` using existing `English` and `Polish` words.",
        request=FlashCardSerializer,
        responses={201: FlashCardSerializer(), 400: None},
    )
    def create(self, request: Request):
        serializer = FlashCardSerializer(data=request.data)
        if serializer.is_valid():
            flashcard = serializer.save()
            return Response(FlashCardSerializer(flashcard).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(exclude=True)
    def update(self, request, pk):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def partial_update(self, request, pk):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, pk):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(tags=["FlashCards"])
class CreateFullyFlashCards(viewsets.ModelViewSet):
    """
    API endpoint to create FlashCards along with new English & Polish words.
    """

    @extend_schema(
        summary="Creates a Flashcard with new words.",
        description="Creates both `English` and `Polish` words and a `FlashCard` linking them.",
        request=RequestFullFlashCardSerializer,
        examples=[
            OpenApiExample(
                "Creates FlashCard Example",
                description="Example request to create a new flashcard with English and Polish words.",
                value={
                    "english_word": {
                        "word": "apple",
                        "description": "A round fruit with red or green skin."
                    },
                    "polish_word": {
                        "word": "jabłko",
                        "description": "Okrągły owoc o czerwonej lub zielonej skórce."
                    }
                },
                request_only=True,  # Example only applies to request body
            ),
        ],

        responses={201: FlashCardSerializer(), 400: None},
    )
    def create(self, request):
        try:
            data_english = request.data["english_word"]
            data_polish = request.data["polish_word"]
        except KeyError as e:
            logger.warning(f"Missing field: {e}")
            return Response({"error": f"Missing field: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        english_word, _ = English.objects.get_or_create(
            word=data_english["word"],
            defaults={"description": data_english.get("description", "")}
        )
        polish_word, _ = Polish.objects.get_or_create(
            word=data_polish["word"],
            defaults={"description": data_polish.get("description", "")}
        )

        flashcard, _ = FlashCard.objects.get_or_create(
            english_word=english_word,
            polish_word=polish_word
        )

        serializer = FlashCardSerializer(flashcard)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(exclude=True)
    def retrieve(self, request, pk):
        flashcard = get_object_or_404(FlashCard, pk=pk)
        serializer = FlashCardSerializer(flashcard)
        return Response(serializer.data)

    @extend_schema(exclude=True)
    def update(self, request, pk):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def partial_update(self, request, pk):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, pk):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def list(self, request):
        return Response({"detail": "Not implemented"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
