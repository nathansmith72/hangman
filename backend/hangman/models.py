import requests
from django.conf import settings
from django.db import models

from accounts.models import User


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=300)

    @classmethod
    def create_word(cls, user):
        random_word = cls.get_random_word()
        # Make sure word does not have a hyphen or capital letter.
        while '-' in random_word or any(x.isupper() for x in random_word):
            random_word = cls.get_random_word()
        return Word.objects.create(
            user=user,
            word=random_word
        )

    @classmethod
    def get_random_word(self):
        wordnik_api_key = settings.WORDNIK_API_KEY
        return requests.get(
            'http://api.wordnik.com/v4/words.json/randomWords'
            '?hasDictionaryDef=true'
            '&minCorpusCount=0'
            '&minLength=5'
            '&maxLength=300'
            '&limit=1'
            '&api_key=%s' % wordnik_api_key
        ).json()[0]['word']


class Guess(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    guess = models.CharField(max_length=1)
    correct = models.BooleanField()

    @property
    def is_correct(self):
        return self.guess in self.word.word

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.correct = self.is_correct
        super().save(force_insert, force_update, using, update_fields)


