<template>
    <div class="input-wrapper">
        <button class="icon"> 
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" height="20px" width="20px">
            <path stroke-linejoin="round" stroke-linecap="round" stroke-width="1.5" stroke="#fff" d="M11.5 21C16.7467 21 21 16.7467 21 11.5C21 6.25329 16.7467 2 11.5 2C6.25329 2 2 6.25329 2 11.5C2 16.7467 6.25329 21 11.5 21Z"></path>
            <path stroke-linejoin="round" stroke-linecap="round" stroke-width="1.5" stroke="#fff" d="M22 22L20 20"></path>
        </svg>
        </button>
        <input v-model="searchTerm" placeholder="search.." class="input" name="text" type="text" @keyup.enter="onSearch">
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const searchTerm = ref('')  // Esta variable almacenará el texto de búsqueda
const router = useRouter()

// Función que se ejecuta cuando se presiona Enter en el search bar
const onSearch = () => {
router.push({ 
name: 'ProductPage', 
query: { search: searchTerm.value || undefined } // 👈 esto limpia el query si está vacío
})
}
</script>

<style src="../../assets/css/Header/search.css" scoped></style>
