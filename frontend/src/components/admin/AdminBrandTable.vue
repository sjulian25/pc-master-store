<template>
    <div>
    <h2>Marcas</h2>
    <button class="create-btn" @click="showCreate = true">Crear Marca</button>
    <table class="admin-table">
        <thead>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="cat in brands" :key="cat.id_brand">
            <td>{{ cat.id_brand }}</td>
            <td>{{ cat.name }}</td>
            <td>
            <button class="edit-btn"@click="openEditModal(cat)">Editar</button>
            <button class="delete-btn" @click="deleteBrand(cat.id_brand)">Eliminar</button>
            </td>
        </tr>
        </tbody>
    </table>
    <div v-if="showCreate" class="modal">
        <form @submit.prevent="createBrand">
            <div class="modal-header">
                <h3>Crear Marca</h3>
            </div>
        <label for="brandName">Nombre de la marca:</label>
        <input
            id="brandName"
            v-model="newBrandName"
            type="text"
            required
            placeholder="Ej: Asus"
        />
        <div class="modal-actions">
            <button type="submit" class="edit-btn" >Crear</button>
            <button type="button" class="delete-btn" @click="closeModal">Cancelar</button>
        </div>
        <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>
        </form>
    </div>
    <div v-if="showEdit" class="modal">
        <form @submit.prevent="updateBrand">
            <div class="modal-header">
                <h3>Editar Marca</h3>
            </div>
        <label for="editCatName">Nombre:</label>
        <input
            id="editCatName"
            v-model="editCat.name"
            type="text"
            required
            placeholder="Ej: Ryzen"
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

const brands = ref([])
const showCreate = ref(false)
const newBrandName = ref('')
const errorMsg = ref('')
const showEdit = ref(false)
const editCat = ref({ id_category: null, name:''})

function openEditModal(cat) {
    editCat.value = { ...cat }
    showEdit.value = true
}

async function updateBrand() {
    errorMsg.value = ''
    if (!editCat.value.name.trim()) {
        errorMsg.value = 'Todos los campos son requeridos'
        return
    }
    try {
        await api.put(`/catalog/brand/${editCat.value.id_brand}`,{
            name : editCat.value.name,
        })
        await fetchBrands()
            closeEditModal()
    }catch (e) {
        errorMsg.value = 'Error al editar la marca'
    }
}

function closeEditModal() {
    showEdit.value = false
    editCat.value = { id_brand: null, name: ''}
    errorMsg.value = ''
}

async function deleteBrand(id) {
    if (!confirm('¿Seguro que deseas eliminar esta marca?')) return
    try {
        await api.delete(`/catalog/brand/${id}`)
        await fetchBrands()
    } catch (e) {
        errorMsg.value = 'Error al eliminar la categoría'
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

async function createBrand() {
    errorMsg.value = ''
    if (!newBrandName.value.trim()) {
    errorMsg.value = 'El nombre es requerido'
    return
    }
    try {
    await api.post('/catalog/brand', { name: newBrandName.value })
    await fetchBrands()
    closeModal()
    } catch (e) {
    errorMsg.value = 'Error al crear la marca'
    }
}

function closeModal() {
    showCreate.value = false
    newBrandName.value = ''
    errorMsg.value = ''
}

onMounted(fetchBrands)
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