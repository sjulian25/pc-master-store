<template>
    <div class="admin-layout">
    <AdminSidebar />
    <div class="admin-content">
        <router-view />
    </div>
    </div>
</template>
<script setup>
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
</script>
<style scoped>
.admin-layout {
    display: flex;
    min-height: 100vh;
    background: #f5f6fa;
}
.admin-content {
    flex: 1;
    padding: 2rem;
}
</style>