<template>
<div class="product-detail">
    <div class="left-column">
    <img :src="product.image || '/img/product/imagedefault.webp'" alt="Imagen del producto" />
    </div>
    <div class="right-column">
    <p>{{ product.name }}</p>
    <p><strong>Categoría:</strong> {{ product.id_type_product }}</p>
    <p><strong>Marca:</strong> {{ brand.name || 'Cargando...' }}</p>
    <p><strong>En Stock:</strong> {{ product.stock }}</p>
    <p class="price">${{ product.price }}</p>
    <button @click="addToCart">Añadir al carrito</button>
    </div>
</div>
<div class="description-box">
    <h3>Descripción del producto</h3>
    <p>{{ product.description }}</p>
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
display: flex;
gap: 2rem;
max-width: 1000px;
margin: 2rem auto;
padding: 1rem;
background-color: var(--ch-c-gray-dark);
border-radius: 12px;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.left-column {
flex: 1;
}

.left-column img {
width: 100%;
border-radius: 12px;
object-fit: cover;
}

.right-column {
flex: 1;
display: flex;
flex-direction: column;
justify-content: space-between;
gap: 1rem;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.right-column p {
margin: 0;
font-size: 1rem;
}

.price {
font-size: 1rem;
color: var(--ch-c-yellow);
font-weight: bold;
}

button {
background-color: var(--ch-c-yellow);
color: #222831;
border: none;
padding: 0.8rem;
font-size: 1.2rem;
border-radius: 8px;
cursor: pointer;
transition: 0.3s;
}

button:hover {
background-color: #e0b94c;
}

.description-box {
max-width: 1000px;
margin: 1rem auto;
padding: 1.5rem;
background-color: var(--ch-c-gray-dark);
border-radius: 12px;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.description-box h3 {
margin-bottom: 0.5rem;
}

.description-box p {
color: var(--ch-c-black);
line-height: 1.6;
font-weight: bold;
}
</style>
