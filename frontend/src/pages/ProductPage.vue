<template>
<v-main>
    <div class="product-page">
    <!-- Breadcrumb en la parte superior -->
    <Breadcrumb />

    <!-- Wrapper horizontal para sidebar + productos -->
    <div class="content-wrapper">
        <!-- Sidebar izquierda -->
        <div class="filter-sidebar">
        <!-- Filtro de categorías -->
        <filtersidebar @filter-by-category="handleFilter" />
        
        <!-- Filtro de precio debajo del filtro de categorías -->
        <filterprice @filter-by-price="handlePriceFilter" />
        </div>

        <!-- Contenido de productos -->
        <div class="product-list">
        <h1 class="title">Productos</h1>
        <div class="products-grid">
            <ProductCard
            v-for="product in filteredProduct"
            :key="product.id_product"
            :product="product"
            @click="goToProductDetail(product.id_product)"
            />
        </div>
        </div>
    </div>
    </div>
</v-main>
</template>


<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import ProductCard from '@/components/product/ProductCard.vue'
import { getAllProducts } from '@/services/productService'
import Breadcrumb from '@/components/layout/Breadcrumb.vue'
import filtersidebar from '@/components/product/filtersidebar.vue'
import filterprice from '@/components/product/filterprice.vue'

const products = ref([])
const router = useRouter()
const route = useRoute()

const goToProductDetail = (id) => {
router.push({ name: 'ProductDetail', params: { id } })
}
const searchTerm = ref(route.query.search || '') // Tomamos el término de búsqueda desde la URL
const normalizeText = (text) => {
  return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase()
}
onMounted(async () => {
try {
    const response = await getAllProducts()
    products.value = response.data || response
} catch (error) {
    console.error('Error al obtener productos:', error)
}
})
const selectedCategoryId = ref(null)
// Función que se activa cuando FilterSidebar emite un filtro
function handleFilter(categoryId) {
selectedCategoryId.value = categoryId || null
}

// Computed que devuelve los productos filtrados
const filteredProduct = computed(() => {
let result = products.value

// Filtrar por término de búsqueda solo si hay algo escrito
if (searchTerm.value.trim()) {
    const search = normalizeText(searchTerm.value)

    result = result.filter(p =>
      (p.name && normalizeText(p.name).includes(search)) ||
      (p.brand?.name && normalizeText(p.brand.name).includes(search)) ||
      (p.category?.name && normalizeText(p.category.name).includes(search))
    )
  }
// Filtrar por categoría
if (selectedCategoryId.value) {
result = result.filter(p => p.id_type_product === selectedCategoryId.value)
}

// Filtrar por precio
if (selectedPriceRange.value.min !== null) {
result = result.filter(p => p.price >= selectedPriceRange.value.min)
}

if (selectedPriceRange.value.max !== null) {
result = result.filter(p => p.price <= selectedPriceRange.value.max)
}

return result
})

const selectedPriceRange = ref({ min: null, max: null })

// Función para manejar el evento del filtro de precio
function handlePriceFilter(range) {
  if (range.min === null && range.max === null) {
    // Si los valores de min y max son null, significa que se ha limpiado el filtro de precio
    selectedPriceRange.value = { min: null, max: null }  // Esto restablece el filtro
  } else {
    // Si se reciben valores válidos, aplicamos el filtro
    selectedPriceRange.value = range
  }
}
// Observar los cambios en el parámetro `search` de la URL
watch(() => route.query.search, (newSearch) => {
  searchTerm.value = newSearch || '' // Actualiza el término de búsqueda
}, { immediate: true })


</script>

<style scoped>
.title {
margin-bottom: 20px;
}
.product-page {
max-width: 1400px;
margin: 0 auto;
padding: 20px 20px 20px 0;
}

/* Breadcrumb separado del contenido */
.breadcrumb {
margin-bottom: 1rem;
}

/* Wrapper que usa flexbox para alinear sidebar y productos */
.content-wrapper {
display: flex;
gap: 20px;
}

/* Sidebar (filtros de categoría y precio) */
.filter-sidebar {
display: flex;
flex-direction: column;
gap: 20px; /* Espacio entre los filtros */
width: 250px;
flex-shrink: 0;
}

/* Productos ocupan el resto del espacio */
.product-list {
flex: 1;
}

/* Grilla de productos */
.products-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 20px;
}
</style>