<template>
    <div>
    <h2>Categorías</h2>
    <button class="create-btn" @click="showCreate = true">Crear Categoría</button>
    <table class="admin-table">
        <thead>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="cat in categories" :key="cat.id_category">
            <td>{{ cat.id_category }}</td>
            <td>{{ cat.name }}</td>
            <td>{{ cat.description }}</td>
            <td>
            <button class="edit-btn" @click="openEditModal(cat)">Editar</button>
            <button class="delete-btn" @click="deleteCategory(cat.id_category)">Eliminar</button>
            </td>
        </tr>
        </tbody>
    </table>
    <div v-if="showCreate" class="modal">
        <h3>Crear Categoría</h3>
        <form @submit.prevent="createCategory">
        <label for="catName">Nombre:</label>
        <input
            id="catName"
            v-model="newCatName"
            type="text"
            required
            placeholder="Ej: Laptops"
        />
        <label for="catDesc">Descripción:</label>
        <input
            id="catDesc"
            v-model="newCatDesc"
            type="text"
            required
            placeholder="Descripción de la categoría"
        />
        <div class="modal-actions">
            <button type="submit" class="edit-btn">Crear</button>
            <button type="button" class="delete-btn" @click="showCreate = false">Cancelar</button>
        </div>
        <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
        </form>
    </div>
    <div v-if="showEdit" class="modal">
        <form @submit.prevent="updateCategory">
        <h3>Editar Categoría</h3>
        <label for="editCatName">Nombre:</label>
        <input
            id="editCatName"
            v-model="editCat.name"
            type="text"
            required
            placeholder="Ej: Laptops"
        />
        <label for="editCatDesc">Descripción:</label>
        <input
            id="editCatDesc"
            v-model="editCat.description"
            type="text"
            required
            placeholder="Descripción de la categoría"
        />
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
import '@/assets/css/admin/admin-table.css'
import api from '@/services/api'

const categories = ref([])
const showCreate = ref(false)
const newCatName = ref('')
const newCatDesc = ref('')
const errorMsg = ref('')
const showEdit = ref(false)
const editCat = ref({ id_category: null, name:'', description: '' })

function openEditModal(cat) {
    editCat.value = { ...cat }
    showEdit.value = true
}

async function updateCategory() {
    errorMsg.value = ''
    if (!editCat.value.name.trim() || !editCat.value.description.trim()) {
        errorMsg.value = 'Todos los campos son requeridos'
        return
    }
    try {
        await api.put(`/catalog/category/${editCat.value.id_category}`,{
            name : editCat.value.name,
            description: editCat.value.description
        })
        await fetchCategories()
        closeEditModal()
    }catch (e) {
        errorMsg.value = 'Error al editar la categoria'
    }
}
function closeEditModal() {
    showEdit.value = false
    editCat.value = { id_category: null, name: '', description: '' }
    errorMsg.value = ''
}

async function deleteCategory(id) {
    if (!confirm('¿Seguro que deseas eliminar esta categoría?')) return
    try {
        await api.delete(`/catalog/category/${id}`)
        await fetchCategories()
    } catch (e) {
        errorMsg.value = 'Error al eliminar la categoría'
    }
}

async function fetchCategories() {
    try {
    const response = await api.get('/catalog/category')
    // El backend devuelve response.data.detailed como array de categorías
    categories.value = response.data.detail || response.data.detailed || response.data || []
    } catch (e) {
        categories.value = []
    }
}

async function createCategory() {
    errorMsg.value = ''
    if (!newCatName.value.trim() || !newCatDesc.value.trim()) {
    errorMsg.value = 'Todos los campos son requeridos'
    return
    }
    try {
    await api.post('/catalog/category', {
        name: newCatName.value,
        description: newCatDesc.value
    })
    await fetchCategories()
    newCatName.value = ''
    newCatDesc.value = ''
    showCreate.value = false
    } catch (e) {
    errorMsg.value = e.response?.data?.message || 'Error al crear la categoría'
    }
}

onMounted(fetchCategories)
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