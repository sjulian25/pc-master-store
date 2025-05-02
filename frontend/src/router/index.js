import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import Default from "@/components/layout/Default.vue";
import ProductDetail from "@/components/product/ProductDetail.vue";
import ProductPage from "@/pages/ProductPage.vue";
// import Catalog from "@/pages/Catalog.vue";
// import ProductPage from "@/pages/ProductPage.vue";
import Login from "@/pages/Login.vue";
import Register from "@/pages/Register.vue";
import AdminDashboard from '@/pages/AdminDashboard.vue'
import AdminProducts from '@/pages/AdminProducts.vue'
import AdminBrands from '@/pages/AdminBrands.vue'
import AdminCategories from '@/pages/AdminCategories.vue'

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
                path: '/ProductPage/product/:id',
                name: 'ProductDetail',
                component: ProductDetail,
                props:true
                
            },
            {
                path: '/admin',
                component: AdminDashboard,
                children: [
                    { path: '', name: 'AdminSummary', component: () => import('@/components/admin/AdminSummary.vue') },
                    { path: 'products', name: 'AdminProducts', component: AdminProducts },
                    { path: 'brands', name: 'AdminBrands', component: AdminBrands },
                    { path: 'categories', name: 'AdminCategories', component: AdminCategories }
                ]
            }


        ]
    },
    
    
    // { path: '/catalog', component: Catalog },
    // { path: '/product', component: ProductPage },
    { 
        path: '/login', 
        name: 'Login',
        component: Login },
    { 
        path: '/register', 
        name: 'Register',
        component: Register },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;