import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm'
import store from './store/index.js'

Vue.config.productionTip = false

Vue.use(BootstrapVue);

new Vue({
  router: router,
  render: h => h(App),
  store: store
}).$mount('#app')
