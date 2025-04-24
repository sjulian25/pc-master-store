<template>
<div class="product-card" @click="handleClick">
    <img :src="product.imageUrl" :alt="product.name" class="product-image" />
    <h3>{{ product.name }}</h3>
    <p>{{ product.description }}</p>
    <span class="price">${{ product.price }}</span>
</div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
product: {
    type: Object,
    required: true
}
})

const emit = defineEmits()

// Emitir un evento de clic hacia el componente padre
const handleClick = () => {
emit('click', props.product.id_product) // Emitimos el id del producto
}
</script>

<style scoped>
.product-card {
cursor: pointer;
border: 1px solid #ccc;
padding: 10px;
text-align: center;
border-radius: 8px;
}

.product-card:hover {
background-color: #f0f0f0;
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
