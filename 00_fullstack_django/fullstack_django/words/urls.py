from django.urls import path
from words.views import (
    EnglishWords,
    EnglishWordDetail,
    PolishWords,
    PolishWordDetail
)

urlpatterns = [
    path("english/", EnglishWords.as_view(), name="english_words"),
    path("english/<int:word_id>/", EnglishWordDetail.as_view(), name="english_word"),
    path("polish/", PolishWords.as_view(), name="polish_words"),
    path("polish/<int:word_id>/", PolishWordDetail.as_view(), name="polish_word"),
]
