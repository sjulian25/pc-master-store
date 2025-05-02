<template>
    <div>
    <h2>Productos</h2>
    <button class="create-btn" @click="showCreate = true">Crear Producto</button>
    <table class="admin-table">
        <thead>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Precio</th>
            <th>Stock</th>
            <th>Marca</th>
            <th>Categoría</th>
            <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="prod in productos" :key="prod.id_product">
            <td>{{ prod.id_product }}</td>
            <td>{{ prod.name }}</td>
            <td>{{ prod.description }}</td>
            <td>${{ prod.price }}</td>
            <td>{{ prod.stock }}</td>
            <td>
                {{ brands.find(b => b.id_brand === prod.id_brand)?.name || 'Sin marca' }}
            </td>
            <td>
                {{ categories.find(c => c.id_type_product === prod.id_type_product)?.name || 'Sin categoría' }}
            </td>
            <td>
                <button class="edit-btn" @click="openEditModal(prod)">Editar</button>
                <button class="delete-btn" @click="deleteProduct(prod.id_product)">Eliminar</button>
            </td>
        </tr>
        </tbody>
    </table>
    <div v-if="showCreate" class="modal">
        <form @submit.prevent="createProduct">
            <div class="modal-header">
                <h3>Crear Producto</h3>
            </div>
        <label for="prodName">Nombre:</label>
        <input id="prodName" v-model="newProd.name" type="text" required placeholder="Ej: Laptop" />

        <label for="prodDesc">Descripción:</label>
        <input id="prodDesc" v-model="newProd.description" type="text" required placeholder="Descripción" />

        <label for="prodPrice">Precio:</label>
        <input id="prodPrice" v-model="newProd.price" type="number" min="0" step="0.01" required placeholder="Precio" />

        <label for="prodStock">Stock:</label>
        <input id="prodStock" v-model="newProd.stock" type="number" min="0" required placeholder="Stock" />

        <label for="prodBrand">Marca:</label>
        <select id="prodBrand" v-model="newProd.id_brand" required>
            <option value="" disabled>Selecciona una marca</option>
            <option v-for="brand in brands" :key="brand.id_brand" :value="brand.id_brand">
            {{ brand.name }}
            </option>
        </select>

        <label for="prodCategory">Categoría:</label>
        <select id="prodCategory" v-model="newProd.id_type_product" required>
            <option value="" disabled>Selecciona una categoría</option>
            <option v-for="cat in categories" :key="cat.id_type_product" :value="cat.id_type_product">
            {{ cat.name }}
            </option>
        </select>

        <div class="modal-actions">
            <button type="submit" class="edit-btn">Crear</button>
            <button type="button" class="delete-btn" @click="showCreate = false">Cancelar</button>
        </div>
        <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
        </form>
    </div>
    <div v-if="showEdit" class="modal">
        <form @submit.prevent="updateProduct">
            <div class="modal-header">
                <h3>Editar Producto</h3>
            </div>
        <label for="prodName">Nombre:</label>
        <input id="prodName" v-model="editCat.name" type="text" required placeholder="Ej: Laptop" />

        <label for="prodDesc">Descripción:</label>
        <input id="prodDesc" v-model="editCat.description" type="text" required placeholder="Descripción" />

        <label for="prodPrice">Precio:</label>
        <input id="prodPrice" v-model="editCat.price" type="number" min="0" step="0.01" required placeholder="Precio" />

        <label for="prodStock">Stock:</label>
        <input id="prodStock" v-model="editCat.stock" type="number" min="0" required placeholder="Stock" />

        <label for="prodBrand">Marca:</label>
        <select id="prodBrand" v-model="editCat.id_brand" required>
            <option value="" disabled>Selecciona una marca</option>
            <option v-for="brand in brands" :key="brand.id_brand" :value="brand.id_brand">
            {{ brand.name }}
            </option>
        </select>

        <label for="prodCategory">Categoría:</label>
        <select id="prodCategory" v-model="editCat.id_type_product" required>
            <option value="" disabled>Selecciona una categoría</option>
            <option v-for="cat in categories" :key="cat.id_type_product" :value="cat.id_type_product">
            {{ cat.name }}
            </option>
        </select>

        <div class="modal-actions">
            <button type="submit" class="edit-btn">Guardar</button>
            <button type="button" class="delete-btn" @click="closeEditModal">Cerrar</button>
        </div>
        <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
        </form>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import '@/assets/css/admin/admin-table.css'
import api from '@/services/api'

const productos = ref([])
const brands = ref([])
const categories = ref([])
const showCreate = ref(false)
const errorMsg = ref('')
const newProd = ref({
    name: '',
    description: '',
    price: '',
    stock: '',
    id_brand: '',
    id_type_product: ''
})
const showEdit = ref(false)
const editCat = ref({ 
    name: '',
    description: '',
    price: '',
    stock: '',
    id_brand: null,
    id_type_product: null})


function openEditModal(cat) {
    editCat.value = { ...cat }
    showEdit.value = true
}

async function updateProduct() {
    errorMsg.value = ''
    if (
        !editCat.value.name.trim() ||
        !editCat.value.description.trim() ||
        !editCat.value.price.trim() ||
        !editCat.value.stock.trim() ||
        !editCat.value.id_brand.trim() ||
        !editCat.value.id_type_product
    ) {
        errorMsg.value = 'Todos los campos son requeridos'
        return
    }
    try {
        await api.put(`/catalog/products/${editCat.value.id_product}`, {
            name: editCat.value.name,
            description: editCat.value.description,
            price: parseFloat(editCat.value.price),
            stock: parseInt(editCat.value.stock),
            id_brand: parseInt(editCat.value.id_brand),
            id_type_product: parseInt(editCat.value.id_type_product)
        })
        await fetchProducts()
            closeEditModal()
    }catch (e) {
        errorMsg.value = 'Error al editar el producto'
    }
}

function closeEditModal() {
    showEdit.value = false
    editCat.value = { id_brand: null, name: ''}
    errorMsg.value = ''
}

async function deleteProduct(id) {
    if (!confirm('¿Seguro que deseas eliminar este Producto?')) return
    try {
        await api.delete(`/catalog/products/${id}`)
        await fetchProducts()
    } catch (e) {
        errorMsg.value = 'Error al eliminar el producto'
    }
}

async function fetchProducts() {
    try {
    const response = await api.get('/catalog/products')
    // Si response.data es un array:
    const data = Array.isArray(response.data) ? response.data : (response.data.detailed || [])
    productos.value = data.map(p => ({
        ...p,
        brand_name: p.brand_name || p.brand || '',
        category_name: p.category_name || p.category || ''
    }))
    } catch (e) {
    productos.value = []
    }
}

async function fetchBrands() {
    try {
    const response = await api.get('/catalog/brand')
    brands.value = response.data.detailed
    } catch (e) {
    brands.value = []
    }
}


async function fetchCategories() {
    try {
        const response = await api.get('/catalog/type_products')
        let data = Array.isArray(response.data)
            ? response.data
            : (response.data.detail || response.data.detailed || [])
        // Transforma cada array en un objeto
        categories.value = data.map(arr => ({
            id_type_product: arr[0], // o id_category si así lo usas
            id_parent: arr[1],
            name: arr[2],
            status: arr[3]
        }))
        console.log('Categorías transformadas:', categories.value)
    } catch (e) {
        categories.value = []
        console.error('Error al cargar categorías:', e)
    }
}

async function createProduct() {
    errorMsg.value = ''
    if (
    !newProd.value.name.trim() ||
    !newProd.value.description.trim() ||
    !newProd.value.price ||
    !newProd.value.stock ||
    !newProd.value.id_brand ||
    !newProd.value.id_type_product
    ) {
    errorMsg.value = 'Todos los campos son requeridos'
    return
    }
    try {
    await api.post('/catalog/products', {
        name: newProd.value.name,
        description: newProd.value.description,
        price: parseFloat(newProd.value.price),
        stock: parseInt(newProd.value.stock),
        id_brand: parseInt(newProd.value.id_brand),
        id_type_product: parseInt(newProd.value.id_type_product) 
    })
    await fetchProducts()
    Object.assign(newProd.value, {
        name: '',
        description: '',
        price: '',
        stock: '',
        id_brand: '',
        id_type_product: ''
    })
    showCreate.value = false
    } catch (e) {
    errorMsg.value = 'Error al crear el producto'
    }
}

onMounted(() => {
    fetchProducts()
    fetchBrands()
    fetchCategories()
})
</script>

<style scoped>
.modal {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 100;
}
.modal form {
    background: #fff;
    padding: 2.5rem 2rem 2rem 2rem;
    border-radius: 16px;
    min-width: 340px;
    max-width: 95vw;
    max-height: 90vh;         
    overflow-y: auto;         
    box-shadow: 0 4px 24px rgba(0,0,0,0.18);
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    position: relative;
}

.modal-actions {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
}
.error-msg {
    color: #ff4444;
    font-size: 0.95rem;
    margin-top: 0.5rem;
}
</style>