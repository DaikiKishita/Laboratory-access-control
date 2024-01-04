import { createRouter, createWebHistory } from 'vue-router'
import NewUser from '../views/NewUser.vue'
import Base from '../views/BaseView.vue'
import DeleteUser from '../views/DeleteUser.vue'

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
  },
  {
    path: '/delete_user',
    name: 'deleteuser',
    component: DeleteUser
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
