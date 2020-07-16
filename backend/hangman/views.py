from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from hangman.models import Word, Guess
from hangman.serializers import WordSerializer


class WordViewset(CreateModelMixin, GenericViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        word = Word.objects.create_word(user=self.request.user)
        data = WordSerializer(word).data
        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=('post', ), detail=True)
    def guess_letter(self, request):
        letter = request.data.get('letter')
        guess, created = Guess.objects.get_or_create(
            word=self.get_object(),
            guess=letter,
        )
        data = WordSerializer(self.get_object()).data
        data['correct'] = guess.is_correct
        if created:
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
