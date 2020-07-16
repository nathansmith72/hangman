import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Hangman from '../views/Hangman.vue'
import store from '../store/index.js'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Hangman',
    component: Hangman,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.getters.is_logged_in) {
      next({ name: 'Login' })
    } else {
      next() // go to wherever I'm going
    }
  } else {
    next() // does not require auth, make sure to always call next()!
  }
})

export default router
