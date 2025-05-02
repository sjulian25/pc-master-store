<script setup>
import { ref, watch } from 'vue';
import Catalog from './pages/Catalog.vue'
import { useAuthStore } from './services/auth'
</script>

<template>
    <RouterView />
</template>

<style scoped>

</style>
