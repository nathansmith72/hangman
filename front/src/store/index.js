import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

export default new Vuex.Store ({
    state: {
        jwt_token: '',
        logged_in: false,
        user: {}
    },
    mutations: {
        set_user(state, user) {
            state.user = user
        },
        set_jwt_token(state, jwt_token) {
            state.jwt_token = jwt_token
            state.logged_in = true
        },
        logout(state) {
            state.jwt_token = ''
            state.logged_in = false
        }
    },
    getters: {
        get_user: state => {
            return state.user
        },
        is_logged_in: state => {
            return state.logged_in
        },
        get_jwt_token: state => {
            return state.jwt_token
        }
    }
})