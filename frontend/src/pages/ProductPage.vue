<template>
<v-main>
    <div class="product-page">
    <!-- Breadcrumb en la parte superior -->
    <Breadcrumb />

    <!-- Wrapper horizontal para sidebar + productos -->
    <div class="content-wrapper">
        <!-- Sidebar izquierda -->
        <filtersidebar />

        <!-- Contenido de productos -->
        <div class="product-list">
        <h1>Productos</h1>
        <div class="products-grid">
            <ProductCard
            v-for="product in products"
            :key="product.id_product"
            :product="product"
            @click="goToProductDetail(product.id_product)"
            />
        </div>
        </div>
    </div>
    </div>
</v-main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import ProductCard from '@/components/product/ProductCard.vue'
import { getAllProducts } from '@/services/productService'
import Breadcrumb from '@/components/layout/Breadcrumb.vue'
import filtersidebar from '@/components/product/filtersidebar.vue'

const products = ref([])
const router = useRouter()

const goToProductDetail = (id) => {
router.push({ name: 'ProductDetail', params: { id } })
}

onMounted(async () => {
try {
    const response = await getAllProducts()
    products.value = response.data || response
} catch (error) {
    console.error('Error al obtener productos:', error)
}
})
</script>

<style scoped>
.product-page {
max-width: 1400px;
margin: 0 auto;
padding: 20px 20px 20px 0;;
}

/* Breadcrumb separado del contenido */
.breadcrumb {
margin-bottom: 1rem;
}

/* Flex horizontal entre sidebar y productos */
.content-wrapper {
display: flex;
gap: 20px;
}

/* Sidebar ocupa ancho fijo */
.filter-sidebar {
width: 250px;
flex-shrink: 0;
}

/* Productos ocupan el resto del espacio */
.product-list {
flex: 1;
}

/* Grilla de productos */
.products-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 20px;
}
</style>
