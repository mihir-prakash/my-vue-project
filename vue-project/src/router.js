
import { createRouter, createWebHistory } from 'vue-router';
import MainPage from './components/MainPage.vue';
import ProfilePage from './components/ProfilePage.vue';

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage,
  },
  {
    path: '/profile',
    name: 'ProfilePage',
    component: ProfilePage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;