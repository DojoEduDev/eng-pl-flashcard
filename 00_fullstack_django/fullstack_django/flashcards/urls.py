from rest_framework import routers
from django.urls import path

from flashcards.views import FlashCardsViewSet, CreateFullyFlashCards

router = routers.SimpleRouter()
router.register('', FlashCardsViewSet, basename='flashcard')
router.register('createflashcard', CreateFullyFlashCards, basename='createflashcard')
urlpatterns = router.urls
