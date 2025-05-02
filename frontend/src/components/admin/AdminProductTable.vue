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
                    <th>Tipo de Producto</th>
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
                        {{ typeProducts.find(tp => tp.id_type_product === prod.id_type_product)?.name || 'Sin tipo' }}
                    </td>
                    <td>
                        <button class="edit-btn" @click="openEditModal(prod)">Editar</button>
                        <button class="delete-btn" @click="deleteProduct(prod.id_product)">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Modal Crear -->
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

                <label for="prodTypeProduct">Tipo de Producto:</label>
                <select id="prodTypeProduct" v-model="newProd.id_type_product" required>
                    <option value="" disabled>Selecciona un tipo</option>
                    <option v-for="tp in typeProducts" :key="tp.id_type_product" :value="tp.id_type_product">
                        {{ tp.name }}
                    </option>
                </select>

                <div class="modal-actions">
                    <button type="submit" class="edit-btn">Crear</button>
                    <button type="button" class="delete-btn" @click="showCreate = false">Cancelar</button>
                </div>
                <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
            </form>
        </div>

        <!-- Modal Editar -->
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

                <label for="prodTypeProduct">Tipo de Producto:</label>
                <select id="prodTypeProduct" v-model="editCat.id_type_product" required>
                    <option value="" disabled>Selecciona un tipo</option>
                    <option v-for="tp in typeProducts" :key="tp.id_type_product" :value="tp.id_type_product">
                        {{ tp.name }}
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
const typeProducts = ref([])
const showCreate = ref(false)
const showEdit = ref(false)
const errorMsg = ref('')

const newProd = ref({
    name: '',
    description: '',
    price: '',
    stock: '',
    id_brand: '',
    id_type_product: ''
})

const editCat = ref({
    id_product: null,
    name: '',
    description: '',
    price: '',
    stock: '',
    id_brand: '',
    id_type_product: ''
})

async function fetchProducts() {
    try {
        const response = await api.get('/catalog/products')
        const data = Array.isArray(response.data) ? response.data : (response.data.detailed || [])
        productos.value = data
    } catch (e) {
        productos.value = []
    }
}

async function fetchBrands() {
    try {
        const response = await api.get('/catalog/brand')
        brands.value = response.data.detail || response.data.detailed || response.data || []
    } catch (e) {
        brands.value = []
    }
}

async function fetchTypeProducts() {
    try {
        const response = await api.get('/catalog/type-products')
        let data = Array.isArray(response.data)
            ? response.data
            : (response.data.detail || response.data.detailed || [])
        typeProducts.value = data.map(tp =>
            Array.isArray(tp)
                ? {
                    id_type_product: tp[0],
                    id_category: tp[1],
                    name: tp[2]
                }
                : tp
        )
    } catch (e) {
        typeProducts.value = []
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

function openEditModal(prod) {
    editCat.value = { ...prod }
    showEdit.value = true
}

async function updateProduct() {
    errorMsg.value = ''
    if (
        !editCat.value.name.trim() ||
        !editCat.value.description.trim() ||
        !editCat.value.price ||
        !editCat.value.stock ||
        !editCat.value.id_brand ||
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
    } catch (e) {
        errorMsg.value = 'Error al editar el producto'
    }
}

function closeEditModal() {
    showEdit.value = false
    editCat.value = {
        id_product: null,
        name: '',
        description: '',
        price: '',
        stock: '',
        id_brand: '',
        id_type_product: ''
    }
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

onMounted(() => {
    fetchProducts()
    fetchBrands()
    fetchTypeProducts()
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