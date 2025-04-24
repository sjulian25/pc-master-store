<template>
    <v-main>
    <div class="home">
    <h1>Productos</h1>
    <div class="products-grid">
    <ProductCard
        v-for="product in products"
        :key="product.id_product"
        :product="product"
        @click="goToProductDetail(product.id_product)"/>
    </div>
</div></v-main>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import ProductCard from '@/components/product/ProductCard.vue'
import { getAllProducts } from '@/services/productService'

// 1. Declaramos productos como una referencia reactiva
const products = ref([])

// 2. Obtenemos el router para navegar entre rutas
const router = useRouter()

// 3. Función para ir a la vista de detalles del producto
const goToProductDetail = (id) => {
// ⚠️ Este ID se convierte automáticamente en prop gracias a props: true en la ruta
console.log('ID enviado a ProductDetail:', id)
router.push({
name: 'ProductDetail',  // coincide con el name en el archivo del router
params: { id },          // este id se enviará como prop automáticamente
})
}

// 4. Llamamos a la API cuando el componente se monta
onMounted(async () => {
try {
const response = await getAllProducts()
console.log(response)
const data = response.data || response
products.value = data
} catch (error) {
console.error('Error al obtener productos:', error)
}
})
</script>

<style scoped>
.home {
max-width: 1200px;
margin: 0 auto;
padding: 20px;
}

.products-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 20px;
}
</style>
