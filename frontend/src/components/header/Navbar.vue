<template>
    <div class="input">
        <button class="value">
            Inicio
        </button>
        <button class="value">
            Tienda
        </button>
        <button class="value">
            <Dropdown label="Categoria" :items="categorias" @select="handleCategorySelect"/>
        </button>
        <button class="value">
            <Dropdown label="Marcas" :items="marcas" @select="handleCategorySelect"/>
        </button>
    </div>

</template>

<script setup>
import Dropdown from './Dropdown.vue';

// TODO: Modificar para que traiga las marcas y categprías de la api
const categorias = ['Mouse', 'Teclado', 'Fuentes']
const marcas = ['Logitech', 'Razer', 'XPG', 'Corsair', 'Cooler Master', 'Asus', 'MSI', 'Gigabyte']

function handleCategorySelect(item){
    console.log('Seleccionaste: ', item);
}
</script>

<style src="../../assets/css/Header/navbar.css" scoped></style>