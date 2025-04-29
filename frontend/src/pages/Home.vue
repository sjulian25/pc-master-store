
<template>
    <main>
        <Carousel/>
        <LAstproduct/>
        <CarouselLogo/>
    </main>
</template>

<script setup>
    import CarouselLogo from '@/components/home/CarouselLogo.vue';
    import Carousel from '@/components/home/Carousel.vue';
    import LAstproduct from '@/components/home/LAstproduct.vue';
    import { useRouter } from 'vue-router';
</script>

<style scoped>

</style>