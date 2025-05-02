<template>
    <div>
    <h1 class="dashboard-title">Panel de Administración</h1>
    <div class="summary-cards">
        <div class="card summary-product">
        <div>
            <h3>Productos</h3>
            <p>{{ totalProducts }}</p>
        </div>
        </div>
        <div class="card summary-brand">
        <div>
            <h3>Marcas</h3>
            <p>{{ totalBrands }}</p>
        </div>
        </div>
        <div class="card summary-category">
        <div>
            <h3>Categorías</h3>
            <p>{{ totalCategories }}</p>
        </div>
        </div>
        <div class="card summary-typeproducts">
        <div>
            <h3>Tipo de Producto</h3>
            <p>{{ totalTypeProducts }}</p>
        </div>
        </div>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

const totalProducts = ref(0)
const totalBrands = ref(0)
const totalCategories = ref(0)
const totalTypeProducts = ref(0)

async function fetchSummary() {
    try {
        const [prodRes, brandRes, catRes, typRes] = await Promise.all([
            api.get('/catalog/products'),
            api.get('/catalog/brand'),
            api.get('/catalog/category'),
            api.get('/catalog/type-products')
        ])
        totalProducts.value = Array.isArray(prodRes.data) ? prodRes.data.length : (prodRes.data.detailed?.length || prodRes.data.detail?.length || 0)
        totalCategories.value = Array.isArray(catRes.data)? catRes.data.length : (catRes.data.detailed?.length || catRes.data.detail?.length || 0)
        totalBrands.value = Array.isArray(brandRes.data)? brandRes.data.length : (brandRes.data.detailed?.length || brandRes.data.detail?.length || 0)
        totalTypeProducts.value = Array.isArray(typRes.data)? typRes.data.length : (typRes.data.detailed?.length || typRes.data.detail?.length || 0) 
    } catch (e) {
        totalProducts.value = 0
        totalBrands.value = 0
        totalCategories.value = 0
        totalTypeProducts.value = 0
        console.error('Error en fetchSummary:', e)
    }
}

onMounted(fetchSummary)
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
.dashboard-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 2rem;
    color: #222831;
}
.summary-cards {
    display: flex;
    gap: 2rem;
    margin-top: 1rem;
    flex-wrap: wrap;
}
.card {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    padding: 2rem 2.5rem;
    min-width: 200px;
    display: flex;
    align-items: center;
    gap: 1.2rem;
    transition: transform 0.2s;
}
.card:hover {
    transform: translateY(-6px) scale(1.03);
}
.card h3 {
    margin: 0;
    font-size: 1.1rem;
    color: #393E46;
}
.card p {
    margin: 0.3rem 0 0 0;
    font-size: 1.5rem;
    font-weight: bold;
    color: #222831;
}
.summary-product { border-left: 6px solid #FFD369; }
.summary-brand { border-left: 6px solid #4CAF50; }
.summary-category { border-left: 6px solid #2196F3; }
.summary-typeproducts { border-left: 6px solid #9521f3; }
</style>