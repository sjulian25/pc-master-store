<template>
    <div class="carrusel-logo">
        <div
            class="carrusel-logo-contenedor"
            :style="{
                transform: `translateX(-${posicion}px)`,
                transition: animar ? 'transform 0.5s ease' : 'none'
            }"
            ref="contenedorRef"
        >
            <div
                class="carrusel-logo-item"
                v-for="(logo, i) in logosDuplicados"
                :key="i"
            >
                <img :src="logo" alt="Logo" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from "vue";

const logos = [
    "/src/assets/img/home/carouselLogo/Logo1.jpg",
    "/src/assets/img/home/carouselLogo/Logo2.jpg",
    "/src/assets/img/home/carouselLogo/Logo3.jpg",
    "/src/assets/img/home/carouselLogo/Logo4.jpg",
    "/src/assets/img/home/carouselLogo/Logo5.jpg",
    "/src/assets/img/home/carouselLogo/Logo6.jpg",
    "/src/assets/img/home/carouselLogo/Logo7.jpg",
    "/src/assets/img/home/carouselLogo/Logo8.jpg",
    "/src/assets/img/home/carouselLogo/Logo9.jpg",
    "/src/assets/img/home/carouselLogo/Logo10.jpg",
    "/src/assets/img/home/carouselLogo/Logo11.jpg",
    "/src/assets/img/home/carouselLogo/Logo12.jpg",
];

// Duplicamos los logos para el efecto infinito
const logosDuplicados = [...logos, ...logos];

const posicion = ref(0);
const anchoItem = ref(0);
const animar = ref(true);
const contenedorRef = ref(null);
let intervalId = null;

const actualizarAncho = () => {
    const contenedor = document.querySelector('.carrusel-logo-item');
    anchoItem.value = contenedor ? contenedor.offsetWidth : 100;
};

onMounted(async () => {
    await nextTick();
    actualizarAncho();

    intervalId = setInterval(() => {
        animar.value = true;
        posicion.value += anchoItem.value;

        // Cuando llegamos a la mitad (final de los logos originales)
        if (posicion.value >= logos.length * anchoItem.value) {
            // Espera a que termine la transición y resetea sin animación
            setTimeout(() => {
                animar.value = false;
                posicion.value = 0;
            }, 500); // 500ms = duración de la transición
        }
    }, 2000);

    window.addEventListener('resize', actualizarAncho);
});

onUnmounted(() => {
    clearInterval(intervalId);
    window.removeEventListener('resize', actualizarAncho);
});
</script>

<style scoped>
.carrusel-logo {
    width: 100%;
    overflow: hidden;
    height: 100px;
    background-color: #fff;
}
.carrusel-logo-contenedor {
    display: flex;
}
.carrusel-logo-item {
    min-width: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.carrusel-logo-item img {
    max-width: 100%;
    max-height: 80px;
    object-fit: contain;
}
</style>
