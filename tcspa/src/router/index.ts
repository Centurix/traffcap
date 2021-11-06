import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import APIDocs from '../views/APIDocs.vue'
import About from '../views/About.vue'
import Messages from '../views/Messages.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/api_docs',
    name: 'api_docs',
    component: APIDocs
  },
  {
    path: '/',
    name: 'messages',
    component: Messages
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
