<template>
    <div class="default-layout">
        <AppHeader />
        <main class="main-content"><router-view></router-view></main>
        <AppFooter />
    </div>
</template>

<script setup>
import AppHeader from '@/components/layout/AppHeader.vue'
import AppFooter from '@/components/layout/AppFooter.vue'
</script>

<style scoped>
.default-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.main-content {
    flex: 1;
    padding: 2rem 0;
}
</style>