<template>
<div class="filter-sidebar">
    <h3>Filtros</h3>

    <div class="filter-group">
    <h4>Categorías</h4>
    <ul>
        <li v-for="category in categories" :key="category">{{ category }}</li>
    </ul>
    </div>
</div>
</template>

<script setup>
// Simulación de categorías desde base de datos
const categories = [
'Mouse',
'Teclado',
'Pantalla',
'Bafle',
'Tarjeta Gráfica',
'Procesador',
'Fuente de poder',
'Memoria RAM',
'Placa base'
]
</script>

<style scoped>
.filter-sidebar {
width: 250px;
margin-left: 0;
padding: 1rem;
background-color: var(--ch-c-yellow, #FFD369);
color: var(--ch-c-black, #222831);
border-right: 1px solid #ccc;
height: 100%;
box-sizing: border-box;
}

h3, h4 {
margin-top: 0;
color: var(--ch-c-black, #222831);
}

.filter-group {
margin-bottom: 1.5rem;
}

input {
width: 100%;
padding: 6px;
margin-top: 4px;
border: 1px solid #ccc;
border-radius: 4px;
}

ul {
list-style: none;
padding: 0;
}

li {
padding: 6px 0;
cursor: pointer;
}

li:hover {
text-decoration: underline;
}
</style>
