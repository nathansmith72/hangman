import axios  from 'axios'
import store from '../../store/index.js'

var api_root_url = 'hangman.nate-uat.com'

export default {
    getWord() {
        return this.refresh_jwt_token().then(() => {
            return axios.get(
                api_root_url + '/api/hangman/get_word/',{
                    headers: this.getAuthHeaders(),
            }).then(response => {
                return response.data
            }).catch(error => {
                if (error.response.status === 401) {
                    store.commit('logout')
                }
            })
        })
    },

    login(username, password) {
        return axios.post(
            api_root_url + '/api/accounts/auth/login/',
            {username: username, password: password}
        ).then(response => {
                return response.data
            }
        )
    },
    refresh_jwt_token() {
        return axios.post(
            api_root_url + '/api/accounts/auth/refresh_token/',
            {token: store.getters.get_jwt_token}
        ).then(response => {
                store.commit('set_jwt_token', response.data.token)
            }
        )
    },
    getAuthHeaders(){
        return {"Authorization": "jwt " + store.getters.get_jwt_token}
    }
}