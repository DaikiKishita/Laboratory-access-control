import { createRouter, createWebHistory } from 'vue-router'
import NewUser from '../views/NewUser.vue'
import Base from '../views/BaseView.vue'

const routes = [
  {
    path: '/new_user',
    name: 'NewUser',
    component: NewUser
  },
  {
    path: '/',
    name: 'base',
    component: Base
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
