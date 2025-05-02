<template>
  <div class="filter-sidebar">
    <h3>Filtrar por tipos</h3>

    <div class="filter-group">
      <ul class="category-list">
        <!-- Opción para ver todos los productos -->
        <li @click="selectCategory(null)" :class="{ selected: selectedCategory === null }">
          Todos los tipos
        </li>
        <li v-for="category in categories" :key="category.id" @click="selectCategory(category.id)"
          :class="{ selected: selectedCategory === category.id }">
          {{ category.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { getAllTypeProduct } from '@/services/typeProductService'
const emit = defineEmits(['filterByCategory'])  // Declaras el evento

const categories = ref([])
onMounted(async () => {
  try {
    const typeProducts = await getAllTypeProduct();
    console.log('Tipos de producto:', typeProducts)
    categories.value = typeProducts.map(tp => ({
      id: tp.id_type_product,
      name: tp.name
    }))
  } catch (error) {
    console.error('Error al cargar los tipos de producto:', error);
  }
});

// categoría seleccionada
const selectedCategory = ref(null)

function selectCategory(id) {
  selectedCategory.value = id
  emit('filterByCategory', id)   // Emitimos hacia el padre
}
</script>
<style scoped>
.filter-sidebar h3 {
  color: var(--ch-c-white);
  background-color: var(--ch-c-gray-dark);
  font-size: 1.4rem;
  margin-bottom: 16px;
  border-bottom: 2px solid var(--ch-c-yellow);
  padding-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.category-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.category-list li {
  background-color: var(--ch-c-yellow);
  color: var(--ch-c-black);
  padding: 10px 16px;
  margin-bottom: 8px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.category-list li:hover {
  background-color: var(--ch-c-gray-dark);
  color: var(--ch-c-white);
}

.category-list li.selected {
  background-color: var(--ch-c-black);
  color: var(--ch-c-yellow);
  font-weight: bold;
  transform: scale(1.03);
}
</style>