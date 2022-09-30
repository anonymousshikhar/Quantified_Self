import Dashboard from './views/Dashboard.vue'
import Login from './views/Login.vue'
import SignUp from './views/SignUp.vue'
import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        name:'Dashboard',
        component: Dashboard,
        path:'/dashboard'
    },
    {
        name:'SignUp',
        component: SignUp,
        path: '/signup'
    },
    {
        name:'Login',
        component: Login,
        path: '/'
    }
];

let router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router; 