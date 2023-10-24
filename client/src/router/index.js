import { createRouter, createWebHashHistory } from 'vue-router'
import LoginView from '../views/Login.vue'
import MainView from '../views/Main.vue'
import RegisterView from '../views/Register.vue'


/*import router from 'vue-router'
router.beforeEach((to, from, next) => {
  const isAuthenticated = true;  // �ж�������ɶ
  if (to.name !== 'login' && !isAuthenticated) {
    next({ name: 'login' });  // �ض��򵽵�¼����
  } else {
    next();  // ������������
  }
});*/

const routes = [
  { path: '/:pathMatch(.*)*', redirect: '/login' },
  {
    path:'/login',
    name:'login',
    component:LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path:'/main',
    name:'main',
    component:MainView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]
import store from '@/store/index.js';
const router = createRouter({
  history: createWebHashHistory(),
  routes
})
router.beforeEach((to, from, next) => {
  var login = store.getters.status
  // 如果目标路由和当前路由相同，不要返回任何值
  if (to.path === from.path) {
    next()
  }
  // 如果目标路由需要验证登录状态
  else {
    // 如果没有登录，则跳转到登录页面，并传递目标路径
    if (!login) {
      if(to.path!='/login'){
        next({
          path: '/login',
        })
      }
      else{
        next()
      }
    }
    // 如果已经登录，则继续跳转
    else {
      if(to.path==='/login'){
        next({
          path:'/main'
        })
      }
      else{
        next()
      }
    }
  }
})
export default router
