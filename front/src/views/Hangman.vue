<template>
    <div class="row" style="text-align: center;">
        <div class="col-md-2 offset-2">
            <div class="wrong-letter-box" style="margin-top:100px;">
                <span v-for="letter in incorrectLetters" v-bind:key="letter"><img v-bind:src="get_incorrect_letter_image(letter)"></span>
            </div>
            <div v-if="game_over" class="col-md-12" style="text-align:center; margin-top:40px;">
                <button v-on:click="get_word()" class="btn btn-success">New Word</button>
            </div>
        </div>
        <div class="col-md-4">
            <div class="col-md-12" style="margin-bottom: -50px; margin-top: 75px;">
                <div class="row">
                    <div class="col-md-6">
                        <label>Wins</label> {{wins}}
                    </div>
                    <div class="col-md-6">
                        <label>Losses</label> {{losses}}
                    </div>
                </div>
            </div>
            <div class="col-md-12">
                <img v-bind:src="get_hangman_image()" id="hangman-image">
            </div>
        </div>
        <div class="col-md-12">
            <span v-for="(letter, index) in word.word" v-bind:key="index"><img v-bind:src="get_letter_image(letter)"></span>
        </div>
        <div v-if="game_over" class="col-md-12">
            <div class="row">
                <div v-if="won" class="col-md-12" style="text-align:center; margin-top:40px;">
                    <h2>Congratulations. You win!</h2>
                </div>
                <div v-else class="col-md-12" style="text-align:center; margin-top:40px;">
                    <h2>Sorry. You lose!</h2>
                </div>
            </div>
        </div>
        <div class="col-md-12" style="margin-top: 50px;" >
            <div class="row">
                <div class="col-md-12" style="text-align:center;">
                    <button v-on:click="guessLetter('a')" data-value="a" v-bind:class="get_classes_by_letter('a')"><img v-bind:src="get_button_letter_image('a')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('b')" data-value="b" v-bind:class="get_classes_by_letter('b')"><img v-bind:src="get_button_letter_image('b')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('c')" data-value="c" v-bind:class="get_classes_by_letter('c')"><img v-bind:src="get_button_letter_image('c')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('d')" data-value="d" v-bind:class="get_classes_by_letter('d')"><img v-bind:src="get_button_letter_image('d')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('e')" data-value="e" v-bind:class="get_classes_by_letter('e')"><img v-bind:src="get_button_letter_image('e')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('f')" data-value="f" v-bind:class="get_classes_by_letter('f')"><img v-bind:src="get_button_letter_image('f')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('g')" data-value="g" v-bind:class="get_classes_by_letter('g')"><img v-bind:src="get_button_letter_image('g')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('h')" data-value="h" v-bind:class="get_classes_by_letter('h')"><img v-bind:src="get_button_letter_image('h')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('i')" data-value="i" v-bind:class="get_classes_by_letter('i')"><img v-bind:src="get_button_letter_image('i')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('j')" data-value="j" v-bind:class="get_classes_by_letter('j')"><img v-bind:src="get_button_letter_image('j')" style="width:100%;"></button>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" style="text-align:center;">
                    <button v-on:click="guessLetter('k')" data-value="k" v-bind:class="get_classes_by_letter('k')"><img v-bind:src="get_button_letter_image('k')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('l')" data-value="l" v-bind:class="get_classes_by_letter('l')"><img v-bind:src="get_button_letter_image('l')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('m')" data-value="m" v-bind:class="get_classes_by_letter('m')"><img v-bind:src="get_button_letter_image('m')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('n')" data-value="n" v-bind:class="get_classes_by_letter('n')"><img v-bind:src="get_button_letter_image('n')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('o')" data-value="o" v-bind:class="get_classes_by_letter('o')"><img v-bind:src="get_button_letter_image('o')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('p')" data-value="p" v-bind:class="get_classes_by_letter('p')"><img v-bind:src="get_button_letter_image('p')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('q')" data-value="q" v-bind:class="get_classes_by_letter('q')"><img v-bind:src="get_button_letter_image('q')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('r')" data-value="r" v-bind:class="get_classes_by_letter('r')"><img v-bind:src="get_button_letter_image('r')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('s')" data-value="s" v-bind:class="get_classes_by_letter('s')"><img v-bind:src="get_button_letter_image('s')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('t')" data-value="t" v-bind:class="get_classes_by_letter('t')"><img v-bind:src="get_button_letter_image('t')" style="width:100%;"></button>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" style="text-align:center;">
                    <button v-on:click="guessLetter('u')" data-value="u" v-bind:class="get_classes_by_letter('u')"><img v-bind:src="get_button_letter_image('u')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('v')" data-value="v" v-bind:class="get_classes_by_letter('v')"><img v-bind:src="get_button_letter_image('v')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('w')" data-value="w" v-bind:class="get_classes_by_letter('w')"><img v-bind:src="get_button_letter_image('w')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('x')" data-value="x" v-bind:class="get_classes_by_letter('x')"><img v-bind:src="get_button_letter_image('x')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('y')" data-value="y" v-bind:class="get_classes_by_letter('y')"><img v-bind:src="get_button_letter_image('y')" style="width:100%;"></button>
                    <button v-on:click="guessLetter('z')" data-value="z" v-bind:class="get_classes_by_letter('z')"><img v-bind:src="get_button_letter_image('z')" style="width:100%;"></button>
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
                guessedLetters: [],
                incorrectGuesses: 0,
                incorrectLetters: [],
                word: {},
                wins: 0,
                losses: 0,
                game_over: false,
                won: false
            }
        },
        methods: {
            get_word() {
                HangmanAPI.getWord().then(word => {
                    this.word = word
                    this.guessedLetters = []
                    this.incorrectGuesses = 0
                    this.incorrectLetters = []
                    this.game_over = false
                    this.won = false
                    this.$forceUpdate();
                })
            },
            guessLetter(letter) {
                if (!this.guessedLetters.includes(letter) && this.incorrectGuesses < 7) {
                    HangmanAPI.guessLetter(this.word.id, letter).then(word => {
                        this.word = word
                        let incorrectGuesses = 0
                        let incorrectLetters = []
                        let guessedLetters = []
                        for (let i = 0; i < this.word.guess_set.length; i++) {
                            if (!this.word.guess_set[i].correct) {
                                incorrectGuesses += 1
                                incorrectLetters.push(this.word.guess_set[i].guess)
                            }
                            guessedLetters.push(this.word.guess_set[i].guess)
                        }
                        this.incorrectGuesses = incorrectGuesses
                        this.incorrectLetters = incorrectLetters
                        this.guessedLetters = guessedLetters
                        this.won = !this.word.word.includes('_') && this.incorrectGuesses < 7
                        this.game_over = incorrectGuesses >=7 || this.won
                        if (this.game_over && this.won) {
                            this.wins += 1
                        } else if (this.game_over) {
                            this.losses += 1
                        }
                    })
                }
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
            },
            get_classes_by_letter(letter) {
                let base_classes = 'btn btn-default letter-button'
                if (this.guessedLetters.includes(letter) || this.incorrectGuesses >= 7){
                    return base_classes + ' deactivated'
                }
                return base_classes
            }
        },
        mounted() {
            this.get_word()
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
    .letter-button.deactivated {
        background-color: #575757;
    }
    .letter-image {
        width:30px;
    }
    #hangman-image{
        max-height:500px;
    }
</style>