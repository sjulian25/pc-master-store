<template>
<div class="breadcrumb-container">
    <div class="breadcrumb">
    <span @click="goTo('/')">Inicio</span> &gt;
    <span>Catálogo</span>
    </div>
</div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const goTo = (path) => router.push(path)
</script>

<style scoped>
.breadcrumb-container {
background-color: var(--ch-c-gray-dark, #393E46);
color: var(--ch-c-white, #EEEEEE);
display: flex;
justify-content: center; /* Centra horizontalmente */
align-items: center;     /* Centra verticalmente */
height: 60px;            /* Altura del breadcrumb */
margin-bottom: 1rem;
}

.breadcrumb {
font-size: 14px;
color: var(--ch-c-white, #EEEEEE);
}

.breadcrumb span {
cursor: pointer;
color: var(--ch-c-white, #EEEEEE);
margin: 0 5px;
}

.breadcrumb span:hover {
text-decoration: underline;
}
</style>
