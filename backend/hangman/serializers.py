from rest_framework import serializers

from hangman.models import Word, Guess


class GuessSerializer(serializers.ModelSerializer):
    correct = serializers.SerializerMethodField()

    class Meta:
        model = Guess
        fields = '__all__'

    def get_correct(self, guess):
        return guess.is_correct()


class WordSerializer(serializers.ModelSerializer):
    word = serializers.SerializerMethodField()
    guess_set = GuessSerializer(many=True)

    class Meta:
        model = Word
        fields = '__all__'

    def get_word(self, word):
        obfuscated_word = ''
        guesses = Guess.objects.filter(word=word)
        for letter in word.word:
            if guesses.filter(guess=letter).exists():
                obfuscated_word += letter
            else:
                obfuscated_word += '_'
        return obfuscated_word
