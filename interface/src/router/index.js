import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  
  },
  {
    path: '/menu',
    name: 'menu',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/MenuView.vue'),
   
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/LoginView.vue'),
   
  },
  {
    path: '/signup',
    name: 'signup',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/SignupView.vue'),
   
  },
  {
    path: '/calendar',
    name: 'calendar',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/CalendarView.vue'),
   
  },
  {
    path: '/liste',
    name: 'liste',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/ListeView.vue'),
   
  },
  {
    path: '/event',
    name: 'event',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/EventView.vue'),
   
  },
  {
    path: '/task',
    name: 'task',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "menu" */ '../views/TaskView.vue'),
   
  },
  {
    path: '/modif',
    name: 'modif',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/ModifView.vue'),
   
  },
  {
    path: '/addvac',
    name: 'addvac',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/AddvacView.vue'),
   
  },
  {
    path: '/day',
    name: 'day',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/DayView.vue'),
   
  },
  {
    path: '/courses',
    name: 'courses',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/CoursesView.vue'),
   
  },
  {
    path: '/experiences',
    name: 'experiences',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/ExperiencesView.vue'),
   
  },
  {
    path: '/lectures',
    name: 'lectures',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/LecturesView.vue'),
   
  },
  {
    path: '/revisions',
    name: 'revisions',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/RevisionsView.vue'),
    
  },
  {
    path: '/exptp',
    name: 'exptp',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited. 
    component: () => import(/* webpackChunkName: "menu" */ '../views/ExpTpView.vue'),
    
  },
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
