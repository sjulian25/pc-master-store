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
import { getBrands } from '@/services/brandService';
import Dropdown from './Dropdown.vue';
import { onMounted, ref } from 'vue';

const marcas = ref([]);

onMounted(async () => {
    marcas.value = await getBrands();
})

// TODO: Modificar para que traiga las marcas y categprías de la api
const categorias = ['Mouse', 'Teclado', 'Fuentes']

function handleCategorySelect(item){
    console.log('Seleccionaste: ', item);
}
</script>

<style src="../../assets/css/Header/navbar.css" scoped></style>