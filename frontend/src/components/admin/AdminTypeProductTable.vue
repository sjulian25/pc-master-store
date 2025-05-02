<template>
    <div>
        <h2>Tipos de Producto</h2>
        <button class="create-btn" @click="showCreate = true">Crear Tipo de Producto</button>
        <table class="admin-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Categoría</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="tp in typeProducts" :key="tp.id_type_product">
                    <td>{{ tp.id_type_product }}</td>
                    <td>{{ tp.name }}</td>
                    <td>
                        {{ categories.find(c => c.id_category == tp.id_category)?.name || 'Sin categoría' }}
                    </td>
                    <td>
                        <button class="edit-btn" @click="openEditModal(tp)">Editar</button>
                        <button class="delete-btn" @click="deleteTypeProduct(tp.id_type_product)">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Modal Crear -->
        <div v-if="showCreate" class="modal">
            <form @submit.prevent="createTypeProduct">
                <div class="modal-header">
                    <h3>Crear Tipo de Producto</h3>
                </div>
                <label for="tpName">Nombre:</label>
                <input id="tpName" v-model="newTypeProduct.name" type="text" required placeholder="Ej: Accesorios" />
                <label for="tpCategory">Categoría:</label>
                <select id="tpCategory" v-model="newTypeProduct.id_category" required>
                    <option value="" disabled>Selecciona una categoría</option>
                    <option v-for="cat in categories" :key="cat.id_category" :value="cat.id_category">
                        {{ cat.name }}
                    </option>
                </select>
                <div class="modal-actions">
                    <button type="submit" class="edit-btn">Crear</button>
                    <button type="button" class="delete-btn" @click="closeCreateModal">Cancelar</button>
                </div>
                <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
            </form>
        </div>

        <!-- Modal Editar -->
        <div v-if="showEdit" class="modal">
            <form @submit.prevent="updateTypeProduct">
                <div class="modal-header">
                    <h3>Editar Tipo de Producto</h3>
                </div>
                <label for="editTpName">Nombre:</label>
                <input id="editTpName" v-model="editTypeProduct.name" type="text" required placeholder="Ej: Accesorios" />
                <label for="editTpCategory">Categoría:</label>
                <select id="editTpCategory" v-model="editTypeProduct.id_category" required>
                    <option value="" disabled>Selecciona una categoría</option>
                    <option v-for="cat in categories" :key="cat.id_category" :value="cat.id_category">
                        {{ cat.name }}
                    </option>
                </select>
                <div class="modal-actions">
                    <button type="submit" class="edit-btn">Guardar</button>
                    <button type="button" class="delete-btn" @click="closeEditModal">Cancelar</button>
                </div>
                <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

const typeProducts = ref([])
const categories = ref([])
const showCreate = ref(false)
const showEdit = ref(false)
const errorMsg = ref('')

const newTypeProduct = ref({
    name: '',
    id_category: ''
})

const editTypeProduct = ref({
    id_type_product: null,
    name: '',
    id_category: ''
})

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

async function fetchCategories() {
    try {
        const response = await api.get('/catalog/category')
        categories.value = response.data.detail || []
    } catch (e) {
        categories.value = []
    }
}

async function createTypeProduct() {
    errorMsg.value = ''
    if (!newTypeProduct.value.name.trim() || !newTypeProduct.value.id_category) {
        errorMsg.value = 'Todos los campos son requeridos'
        return
    }
    try {
        await api.post('/catalog/type-products', {
            name: newTypeProduct.value.name,
            id_category: newTypeProduct.value.id_category
        })
        await fetchTypeProducts()
        closeCreateModal()
    } catch (e) {
        errorMsg.value = 'Error al crear el tipo de producto'
    }
}

function openEditModal(tp) {
    editTypeProduct.value = { ...tp }
    showEdit.value = true
    errorMsg.value = ''
}

async function updateTypeProduct() {
    errorMsg.value = ''
    if (!editTypeProduct.value.name.trim() || !editTypeProduct.value.id_category) {
        errorMsg.value = 'Todos los campos son requeridos'
        return
    }
    try {
        await api.put(`/catalog/type-products/${editTypeProduct.value.id_type_product}`, {
            name: editTypeProduct.value.name,
            id_category: editTypeProduct.value.id_category
        })
        await fetchTypeProducts()
        closeEditModal()
    } catch (e) {
        errorMsg.value = 'Error al editar el tipo de producto'
    }
}

async function deleteTypeProduct(id) {
    if (!confirm('¿Seguro que deseas eliminar este tipo de producto?')) return
    try {
        await api.delete(`/catalog/type-products/${id}`)
        await fetchTypeProducts()
    } catch (e) {
        errorMsg.value = 'Error al eliminar el tipo de producto'
    }
}

function closeCreateModal() {
    showCreate.value = false
    newTypeProduct.value = { name: '', id_category: '' }
    errorMsg.value = ''
}

function closeEditModal() {
    showEdit.value = false
    editTypeProduct.value = { id_type_product: null, name: '', id_category: '' }
    errorMsg.value = ''
}

onMounted(() => {
    fetchTypeProducts()
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
    padding: 2rem;
    border-radius: 12px;
    min-width: 320px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
.modal-header {
    width: 100%;
    padding-bottom: 1rem;
    border-bottom: 1.5px solid #FFD369;
    background: #fff;
    border-top-left-radius: 12px;
    border-top-right-radius: 12px;
    text-align: center;
}
.modal-header h3 {
    margin: 0;
    color: #222831;
    font-size: 1.3rem;
    font-weight: bold;
    text-align: center;
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
.create-btn {
    background: #222831;
    color: #FFD369;
    border: none;
    padding: 0.7rem 1.5rem;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1rem;
    margin-bottom: 1.2rem;
    cursor: pointer;
    transition: background 0.2s, color 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 8px rgba(34,40,49,0.08);
    letter-spacing: 0.5px;
}
.create-btn:hover {
    background: #FFD369;
    color: #222831;
    box-shadow: 0 4px 16px rgba(34,40,49,0.13);
}
</style>