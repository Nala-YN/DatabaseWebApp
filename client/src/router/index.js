import { createRouter, createWebHashHistory } from 'vue-router'
import LoginView from '../views/Login.vue'
import MainView from '../views/Main.vue'
import RegisterView from '../components/Register.vue'


/* ����û��Ƿ��Ѿ���¼�����û�е�¼�����û��ض��򵽵�¼ҳ�棺
   to ������ʾ�û�Ҫ�����·�ɣ�from ������ʾ�û����Ե�·�ɣ�
   next �������ڿ���·�ɵ���ת */
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

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
