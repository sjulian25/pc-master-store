
<template>
    <main>
        <Carousel/>
        <LastProduct/>
        <CarouselLogo/>
    </main>
</template>

<script setup>
    import CarouselLogo from '@/components/home/CarouselLogo.vue';
    import Carousel from '@/components/home/Carousel.vue';
    import LastProduct from '@/components/home/LastProduct.vue';
    import { useRouter } from 'vue-router';
</script>

<style scoped>

</style>