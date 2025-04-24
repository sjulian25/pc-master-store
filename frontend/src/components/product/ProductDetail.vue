<template>
<div class="product-detail">
    <img :src="product.image || '/img/product/imagedefault.webp'" />
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <span class="price">${{ product.price }}</span>
    <p>Categoria: {{ product.id_type_product }}</p>
    <p>En Stock: {{ product.stock }}</p>
    <p>Marca: {{ brand.name || 'Cargando...' }}</p>  <!-- Aquí mostramos la marca -->
    <button @click="addToCart">Añadir al carrito</button>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getProductById} from '@/services/productService'
import { getBrandsId } from '@/services/brandService' // Asegúrate de tener estos servicios

const route = useRoute()
const product = ref({})
const brand = ref({})

// Función para obtener los detalles del producto
const fetchProductDetail = async (id) => {
try {
    const productData = await getProductById(id)
    product.value = productData
    // Ahora obtenemos la marca con el id de la marca
    const brandName = await getBrandsId(productData.id_brand); // Obtener solo el nombre de la marca
        console.log(brandName);  // Esto debería mostrar el nombre de la marca
        brand.value = { name: brandName };  // Guardamos el nombre de la marca en 'brand'
    } catch (error) {
        console.error('Error al obtener los detalles del producto:', error);
    }
}

onMounted(() => {
const productId = route.params.id // Obtenemos el id del producto desde la ruta
fetchProductDetail(productId) // Llamamos a la función para obtener el detalle del producto
})

const addToCart = () => {
console.log(`${product.value.name} añadido al carrito`)
}
</script>

<style scoped>
.product-detail {
width: 300px;
padding: 20px;
border: 1px solid #ccc;
margin: 20px;
text-align: center;
}

.product-image {
max-width: 100%;
height: auto;
}

.price {
font-weight: bold;
color: green;
}
</style>
