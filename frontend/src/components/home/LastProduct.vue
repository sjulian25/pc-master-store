<template>
    <div class="productos-recientes">
        <h2>Productos Recientes</h2>
        <div class="productos-lista">
            <ProductCard
                v-for="producto in productos"
                :key="producto.id_product"
                :product="producto"
                @click="goToProductDetail(producto.id_product)"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, } from 'vue'
import { useRouter } from 'vue-router'
import ProductCard from '../product/ProductCard.vue'
import { getAllProducts } from '@/services/productService'
const router = useRouter()

const productos = ref([])

const fetchProductos = async () => {
    const data = await getAllProducts()
    console.log(data)
    // Ordena por fecha descendente (más reciente primero)
    productos.value = [...data].sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
}

onMounted(fetchProductos)
const goToProductDetail = (id) => {
  console.log('ID recibido:', id)  // Asegúrate de que esto imprime el ID correcto
  if (id) {
    router.push({ name: 'ProductDetail', params: { id } })
  } else {
    console.error("El ID del producto no se ha recibido correctamente.")
  }
}
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
    flex-wrap: nowrap;
    gap: 1rem;
}
</style>

