import { createRouter, createWebHashHistory } from 'vue-router'
import LoginView from '../views/Login.vue'
import MainView from '../views/Main.vue'
import RegisterView from '../components/Register.vue'


/* 检查用户是否已经登录，如果没有登录，则将用户重定向到登录页面：
   to 参数表示用户要进入的路由，from 参数表示用户来自的路由，
   next 函数用于控制路由的跳转 */
/*import router from 'vue-router'
router.beforeEach((to, from, next) => {
  const isAuthenticated = true;  // 判断条件是啥
  if (to.name !== 'login' && !isAuthenticated) {
    next({ name: 'login' });  // 重定向到登录界面
  } else {
    next();  // 继续正常导航
  }
});*/

const routes = [
  {  // 将默认路由重定向到登录页面
    path: '/',
    redirect: '/login'
  },
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
    path: '/',
    name: 'Main',
    component: MainView
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

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
