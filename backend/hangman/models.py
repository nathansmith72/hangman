import requests
from django.conf import settings
from django.db import models

from accounts.models import User


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=300)

    @classmethod
    def create_word(cls, user):
        wordnik_api_key = settings.WORDNIK_API_KEY
        random_word = requests.get(
            'http://api.wordnik.com/v4/words.json/randomWords'
            '?hasDictionaryDef=true'
            '&minCorpusCount=0'
            '&minLength=5'
            '&maxLength=300'
            '&limit=1'
            '&api_key=%s' % wordnik_api_key
        ).json()[0]['word']
        return Word.objects.create(
            user=user,
            word=random_word
        )


class Guess(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    guess = models.CharField(max_length=1)

    @property
    def is_correct(self):
        return self.guess in self.word.word
