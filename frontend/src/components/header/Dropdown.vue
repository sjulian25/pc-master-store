<template>
    <div class="dropdown-wrapper" @mouseenter="show=true" @mouseleave="show=false">
        <button class="dropdown-button value">{{ label }}</button>
        <div v-if="show" class="dropdown-menu">
            <p v-for="(item, index) in items" :key="index" @click="handleClick(item)">
                {{ item }}
            </p>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
    label: String,
    items: Array,
})

const emit = defineEmits(['select'])
const show = ref(false)

function handleClick(item){
    emit('select', item)
    show.value = false
}
</script>

<style src="../../assets/css/Header/dropdown.css" scoped></style>