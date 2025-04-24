<template>
<div class="product-detail">
    <img src="../../assets/img/products/mouse_img.webp" alt="Imagen del producto" class="product-image" />
    <div class="product-info">
    <h1>{{ product.name }}</h1>
    <p class="description">{{ product.description }}</p>
    <p class="price">$ {{ product.price }}</p>
    <p class="stock">Stock disponible: {{ product.stock }}</p>
    <p class="brand">Marca ID: {{ product.id_brand }}</p> <!-- o cambia por el nombre si lo tienes -->
    <p class="category">Tipo de producto ID: {{ product.id_type_product }}</p>
    <p class="status" v-if="!product.is_active">Este producto no está disponible actualmente</p>
    <button class="buy-button" :disabled="!product.is_active || product.stock === 0">
        Agregar al carrito
    </button>
    </div>
</div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import getProductById from '@/services/productService'
import getBrandById from '@/services/brandService'

const product = ref({})
const brand = ref({})  // Para almacenar los datos de la marca
const route = useRoute()

onMounted(async () => {
// Obtener el ID del producto desde la URL
const productId = route.params.id

// Obtener los detalles del producto usando el servicio
const productResponse = await getProductById(productId)
product.value = productResponse.data

// Obtener la marca usando el id_brand del producto
const brandResponse = await getBrandById(product.value.id_brand)
brand.value = brandResponse
})
</script>

  
  <style scoped>
  .product-detail {
    display: flex;
    padding: 2rem;
    gap: 2rem;
  }
  .product-image {
    width: 300px;
    border-radius: 12px;
  }
  .product-info {
    flex: 1;
  }
  .description {
    color: #666;
  }
  .price {
    font-weight: bold;
    font-size: 1.2rem;
  }
  .buy-button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    background-color: #FFD369;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
  .buy-button:hover {
    background-color: #ffcb2b;
  }
  </style>
  