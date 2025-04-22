import { createRouter, createWebHistory } from "vue-router";
// import Home from "@/pages/Home.vue";
// import Catalog from "@/pages/Catalog.vue";
// import ProductPage from "@/pages/ProductPage.vue";
// import Login from "@/pages/Login.vue";
// import Register from "@/pages/Register.vue";

const routes = [
    // { path: '/', component: Home },
    // { path: '/catalog', component: Catalog },
    // { path: '/product', component: ProductPage },
    // { path: '/login', component: Login },
    // { path: '/register', component: Register },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;