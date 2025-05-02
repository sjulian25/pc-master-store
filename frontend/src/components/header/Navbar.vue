<template>
    <div class="input">
        <button class="value">
        <router-link to="/" class="value">
        Inicio
        </router-link>
        </button>
        <button class="value">
        <router-link to="/ProductPage" class="value">
        Tienda
        </router-link>
        </button>
        <button class="value">
            <Dropdown label="Categoria" :items="categorias" @select="handleCategorySelect"/>
        </button>
        <button class="value">
            <Dropdown label="Marcas" :items="marcas" @select="handleBrandSelect"/>
        </button>
    </div>

</template>

<script setup>
import { getCategory } from '@/services/categoryService'
import { getBrands } from '@/services/brandService';
import Dropdown from './Dropdown.vue';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router'
const router = useRouter()


const marcas = ref([]);

onMounted(async () => {
    try {
        const response = await getBrands(); // Aseguramos que la respuesta esté bien guardada en la variable 'response'
        marcas.value = response; // Asignamos la respuesta correctamente a 'marcas'
        console.log("asi vienen las marcas:", marcas.value); // Revisa que marcas tenga los valores correctos
    } catch (error) {
        console.error('Error al obtener las marcas:', error);
    }
});

const categorias = ref([]);

onMounted(async () => {
    categorias.value = await getCategory();
    console.log(categorias.value); // Revisa que categorias tenga los valores correctos
})



// Función para manejar selección de categorías
function handleCategorySelect(item) {
    console.log('Seleccionaste la categoría: ', item.name);
    if (item?.name) {
        router.push({
            name: 'ProductPage',
            query: { category: item }  // Pasamos la categoría en la URL
        });
    }
}

// Función para manejar selección de marcas
function handleBrandSelect(item) {
    console.log('Seleccionaste la marca: ', item);
    if (item) {
        router.push({
            name: 'ProductPage',
            query: { brand: item.id_brand }  // Cambiado a 'item' directamente, ya que 'item' es un string en este caso
        });
    }
}
</script>

<style src="../../assets/css/Header/navbar.css" scoped></style>