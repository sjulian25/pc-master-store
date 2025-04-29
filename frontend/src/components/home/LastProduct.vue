<template>
    <div class="productos-recientes">
        <h2>Productos Recientes</h2>
        <div class="productos-lista">
            <ProductCard
                v-for="producto in productos"
                :key="producto.id_product"
                :product="producto"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProductCard from '../product/ProductCard.vue'
import { getAllProducts } from '@/services/productService'

const productos = ref([])

const fetchProductos = async () => {
    const data = await getAllProducts()
    // Ordena por fecha descendente (más reciente primero)
    productos.value = [...data].sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
}

onMounted(fetchProductos)
</script>

<style scoped>
.productos-recientes h2{
    text-align: center;
    font-size: 50px;
    color: var(--ch-c-black);
    -webkit-text-stroke: 0.5px #000000
}
.productos-recientes {
    background-color: var(--ch-c-white);
    padding: 1rem 0;
}
.productos-lista .product-card:hover{
    background-color: var(--ch-c-gray-dark);
}
.productos-lista {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem;
}
</style>