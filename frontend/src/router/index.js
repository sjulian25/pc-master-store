import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import Default from "@/components/layout/Default.vue";
import ProductDetail from "@/components/product/ProductDetail.vue";
import ProductPage from "@/pages/ProductPage.vue";
// import Catalog from "@/pages/Catalog.vue";
// import ProductPage from "@/pages/ProductPage.vue";
// import Login from "@/pages/Login.vue";
// import Register from "@/pages/Register.vue";

const routes = [
    {
        path: '/',
        component: Default,
        children: [
            { 
                path: '/',
                name: 'Home',
                component: Home 
            },
            {
                path: '/ProductPage',
                name: 'ProductPage',
                component: ProductPage  
            },
            {
                path: '/product/:id',
                name: 'ProductDetail',
                component: ProductDetail,
                props:true
                
            },

        ]
    },
    
    
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