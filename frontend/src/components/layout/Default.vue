<template>
    <div class="default-layout">
        <header>
            <AppHeader />
        </header>
        <main class="main-content"><RouterView></RouterView></main>
        <footer>
            <AppFooter />
        </footer>
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