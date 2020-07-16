<template>
    <div class="bg-image">
        <div class="container d-flex h-100">
            <div class="bg-cover"></div>
            <div class="row justify-content-center align-self-center" style="width: 100%;">
                <div class="col-md-4">
                    <div class="card login-card p-4">
                        <div class="card-header">
                            <h2 class="card-title">Login</h2>
                        </div>
                        <div class="card-body">
                            <p>
                                <label for="username">Username:</label>
                                <input v-model="username" class="form-control" type="text" autocomplete="off" required id="username">
                            </p>
                            <p>
                                <label for="password">Password:</label>
                                <input v-model="password" class="form-control" type="password" autocomplete="off" required id="password">
                            </p>
                            <div class="alert alert-danger" v-if="error">Incorrect username or password.</div>
                            <button v-on:click="login">Login</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import HangmanAPI from '@/services/api/Hangman'
    import store from '../store/index.js'
    import router from '../router/index.js'
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
                error: false
            }
        },
        methods: {
            login() {
                HangmanAPI.login(this.username, this.password).then(response => {
                    store.commit('set_jwt_token', response.token)
                    store.commit('set_user', response.user)
                    router.push({ path: '/' })
                }).catch(() => {
                    this.error = true
                })
            }
        }
    }
</script>

<style scoped>
    input {
        width: 100%;
    }
    .bg-image {
        background: linear-gradient( rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7) ), url("../assets/images/city-background.jpeg");
        background-size: cover;
        height: 100vh;
    }
</style>