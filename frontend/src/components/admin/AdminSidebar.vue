<template>
    <aside class="admin-sidebar">
    <div class="sidebar-header">
        <span class="logo">🛒</span>
        <h2>Panel Admin</h2>
    </div>
    <nav>
        <router-link to="/admin" exact-active-class="active">
            Resumen
        </router-link>
        <div>
        <router-link to="/admin/products" exact-active-class="active" @click="toggleProducts">
            Productos
        </router-link>
        <div v-if="showProducts" class="submenu">
            <router-link to="/admin/brands" exact-active-class="active">
                Marcas
            </router-link>
            <router-link to="/admin/categories" exact-active-class="active">
                Categorías
            </router-link>
            <router-link to="/admin/typeproducts" exact-active-class="active">
                Tipos de Producto
            </router-link>
        </div>
        </div>
    </nav>
    </aside>
</template>

<script setup>
import { ref } from 'vue'
import '@/assets/css/admin/admin-table.css'
const showProducts = ref(false)
function toggleProducts() {
    showProducts.value = !showProducts.value
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.admin-sidebar {
    width: 240px;
    min-height: 100vh;
    background: linear-gradient(135deg, #222831 70%, #393E46 100%);
    color: #fff;
    display: flex;
    flex-direction: column;
    padding: 2rem 1rem;
    box-shadow: 2px 0 8px rgba(0,0,0,0.07);
    border-radius: 0 16px 16px 0;
}
.sidebar-header {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 2.5rem;
}
.logo {
    font-size: 2rem;
}
.admin-sidebar h2 {
    font-size: 1.3rem;
    color: #FFD369;
    font-weight: bold;
    margin: 0;
}
.admin-sidebar nav {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}
.admin-sidebar a {
    color: #fff;
    text-decoration: none;
    font-size: 1.08rem;
    padding: 0.7rem 1.2rem;
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    transition: background 0.2s, color 0.2s;
}
.admin-sidebar a.active,
.admin-sidebar a:hover {
    background: #FFD369;
    color: #222831;
    font-weight: bold;
}
.submenu {
    margin-left: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.7rem;
}
</style>