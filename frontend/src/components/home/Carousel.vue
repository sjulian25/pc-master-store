<template>
    <div class="carrusel">
        <div class="carrusel-contenedor" :style="{ transform: `translateX(-${posicion}px)`}">
            <div class="carrusel-item" v-for="(item, index) in items" :key="index">
                <img :src="item.imagen" :alt="item.titulo">
            </div>
        </div>
        <button @click="anterior" class="boton-anterior">←</button>
        <button @click="siguiente" class="boton-siguiente">→</button>
        <div class="carrusel-indicadores">
            <span
                v-for="(items, i) in items"
                :key="i"
                :class="{ activo: posicion === i * anchoItem }"
                @click="posicion = i * anchoItem"
            ></span>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const items = ref([
    { titulo: 'Imagen 1', imagen: '/src/assets/img/home/carousel/publi10.png' },
    { titulo: 'Imagen 2', imagen: '/src/assets/img/home/carousel/publi11.jpg' },
    { titulo: 'Imagen 3', imagen: '/src/assets/img/home/carousel/publi12.jpg' }
]);

const posicion = ref(0);
const anchoItem = ref(0);

const siguiente = () => {
    if (posicion.value < (items.value.length - 1) * anchoItem.value) {
        posicion.value += anchoItem.value;
    }
};

const anterior = () => {
    if (posicion.value > 0) {
        posicion.value -= anchoItem.value;
    }
};

onMounted(() => {
    const contenedor = document.querySelector('.carrusel-contenedor');
    anchoItem.value = contenedor.offsetWidth;
    // Define la funcion para poder removerla despues
    const resizeHandler = () => {
        anchoItem.value = contenedor.offsetWidth;
    };

    window.addEventListener('resize',resizeHandler);
    
    // Limpia el event Listener al desmontar
    onMounted(() => {
        window.removeEventListener('resize', resizeHandler)
    })
    });

</script>

<style scoped>
.carrusel {
    position: relative;
    width: 100vw;           /* Ocupa todo el ancho de la ventana */
    max-width: 100vw;       
    margin: 0;              
    left: 50%;
    right: 50%;
    transform: translateX(-50%);
    overflow: hidden;
    height: 400px;
    border-radius: 0;       /* Opcional: elimina el borde redondeado para pantalla completa */
    box-shadow: 0 4px 24px rgba(0,0,0,0.12);
    z-index: 1;
}

.carrusel-contenedor {
    display: flex;
    transition: transform 0.4s cubic-bezier(.4,0,.2,1);
    max-height: fit-content;
    width: 100vw;           /* Asegura que el contenedor también ocupe todo el ancho */
}

.carrusel-item {
    position: relative;
    min-width: 100%;
    flex-shrink: 0;
    height: 400px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
}

.carrusel-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}


.boton-anterior,
.boton-siguiente {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.6);
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    font-size: 1.5rem;
    cursor: pointer;
    z-index: 10;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    transition: background 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
}
.boton-anterior:hover,
.boton-siguiente:hover {
    background: rgba(0, 0, 0, 0.8);
}
.boton-anterior { left: 10px; }
.boton-siguiente { right: 10px; }

.carrusel-indicadores {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    position: absolute;
    bottom: 16px;
    left: 0;
    width: 100%;
    z-index: 5;
}
.carrusel-indicadores span {
    display: inline-block;
    width: 12px;
    height: 12px;
    margin: 0 4px;
    background: #bbb;
    border-radius: 50%;
    cursor: pointer;
    transition: background 0.3s;
}
.carrusel-indicadores .activo {
    background: #333;
}
</style>