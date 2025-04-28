<template>
<div class="price-filter">
    <!-- Título de la sección "Elegir precio" con estilo similar -->
    <h3 class="price-title">Elegir precio</h3>
    
    <!-- Contenedor de los inputs (min y max) en línea -->
    <div class="inputs">
    <label class="min-price">
        <span class="price-label">Mínimo:</span>
        <input type="number" v-model.number="min" />
    </label>
    
    <label class="max-price">
        <span class="price-label">Máximo:</span>
        <input type="number" v-model.number="max" />
    </label>
    </div>

    <!-- Botón para aplicar el filtro, centrado -->
    <button @click="emitFilter">Aplicar filtro</button>
</div>
</template>

<script setup>
import { ref } from 'vue'

const min = ref(null)
const max = ref(null)

const emit = defineEmits(['filter-by-price'])

function emitFilter() {
emit('filter-by-price', { min: min.value, max: max.value })
}
</script>

<style scoped>
.price-filter {
margin-top: 20px;
padding: 10px;
border-top: 2px solid var(--ch-c-yellow);
}

/* Estilo similar al del sidebar para el título "Elegir precio" */
.price-title {
color: var(--ch-c-white);
background-color: var(--ch-c-gray-dark);
font-size: 1.4rem;
margin-bottom: 16px;
border-bottom: 2px solid var(--ch-c-yellow);
padding-bottom: 8px;
text-transform: uppercase;
letter-spacing: 1px;
}

.inputs {
display: flex;
justify-content: space-between; /* Hace que los inputs se ubiquen a la izquierda y derecha */
gap: 10px;
}

.inputs label {
display: flex;
flex-direction: column;
width: 48%; /* Controla el ancho de cada input */
}

/* Aplica color amarillo al texto de las etiquetas "Mínimo" y "Máximo" */
.price-label {
color: var(--ch-c-yellow);
font-weight: bold;
}

input {
padding: 6px;
border: 1px solid var(--ch-c-gray-dark);
border-radius: 4px;
width: 100%;
background-color: var(--ch-c-gray-dark); /* Fondo gris oscuro */
color: var(--ch-c-white); /* Texto blanco para contraste */
}

button {
margin-top: 10px;
padding: 6px 12px;
background-color: var(--ch-c-yellow);
border: none;
border-radius: 4px;
color: var(--ch-c-black);
font-weight: bold;
cursor: pointer;
display: block; /* Hace que el botón sea un bloque */
margin-left: auto;
margin-right: auto; /* Centra el botón */
}
</style>
