<template>
    <div class="row" style="text-align: center;">
        <div class="col-md-12">
            <img v-bind:src="get_hangman_image()" id="hangman-image">
        </div>
        <div class="col-md-12">
            <span v-for="letter in word" v-bind:key="letter">{{ get_letter_image(letter) }}</span>
        </div>
        <div class="col-md-12">
            <span v-for="letter in incorrectLetters" v-bind:key="letter">{{ get_incorrect_letter_image(letter) }}</span>
        </div>
        <div class="col-md-12" >
            <div class="row">
                <div class="col-md-12" style="text-align:center;">
                    <button v-on:click="guessLetter('a')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('a')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('b')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('b')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('c')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('c')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('d')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('d')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('e')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('e')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('f')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('f')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('g')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('g')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('h')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('h')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('i')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('i')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('j')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('j')" style="width:100%;"></button>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" style="text-align:center;">
                    <button v-on:click="guessLetter('k')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('k')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('l')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('l')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('m')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('m')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('n')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('n')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('o')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('o')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('p')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('p')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('q')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('q')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('r')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('r')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('s')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('s')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('t')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('t')" style="width:100%;"></button>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" style="text-align:center;">
                    <button v-on:click="guessLetter('u')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('u')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('v')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('v')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('w')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('w')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('x')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('x')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('y')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('y')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('z')" class="btn btn-default letter-button"><img v-bind:src="get_button_letter_image('z')" style="width:100%;"></button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import HangmanAPI from '@/services/api/Hangman'
    export default {
        name: "Hangman",
        data () {
            return {
                selectedLetter: '',
                guessedLetters: [],
                incorrectGuesses: 0,
                incorrectLetters: [],
                word_id: 0,
                word: ''
            }
        },
        methods: {
            get_word() {
                HangmanAPI.getWord().then(word => {
                    this.word = word.word
                    this.word_id = word.id
                })
            },
            guessLetter(letter) {
                HangmanAPI.guessLetter(this.word_id, letter).then(result => {
                    if (result.correct) {
                        this.word = result.word
                    } else {
                        this.incorrectGuesses += 1
                        this.incorrectLetters.push(this.selectedLetter)
                    }
                })
            },
            get_hangman_image() {
                return require('../assets/images/hangman/hangman_' + this.incorrectGuesses + '.png')
            },
            get_letter_image(letter) {
                if(letter === '_'){
                    return require('../assets/images/hangman/underscore.png')
                } else {
                    return require('../assets/images/hangman/' + letter + '_underscore.png')
                }
            },
            get_incorrect_letter_image(letter) {
                return require('../assets/images/hangman/' + letter + '_incorrect.png')
            },
            get_button_letter_image(letter) {
                return require('../assets/images/hangman/' + letter + '.png')
            }
        }
    }
</script>

<style scoped>
    .letter-button {
        width:45px;
        height:45px;
        margin-left: 5px;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    .letter-image {
        width:30px;
    }
    #hangman-image{
        max-height:500px;
    }
</style>