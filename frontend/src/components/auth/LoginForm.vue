<script setup>
import { reactive } from 'vue'

const form = reactive({
  name: '',
  email: '',
  password: ''
})

function handleSubmit() {
  // Aquí se enviaría a la API cuando esté lista
  console.log('Datos del formulario:', form)

  // Limpiar formulario
  form.name = ''
  form.email = ''
  form.password = ''
}
</script>

<template>
     <form @submit.prevent="handleSubmit" class="user-form">
    <div class="form-group">
      <label for="name">Nombre</label>
      <input id="name" v-model="form.name" type="text" required />
    </div>

    <div class="form-group">
      <label for="email">Correo electrónico</label>
      <input id="email" v-model="form.email" type="email" required />
    </div>

    <div class="form-group">
      <label for="password">Contraseña</label>
      <input id="password" v-model="form.password" type="password" required />
    </div>

    <button type="submit">Registrar</button>
  </form>
</template>

<style>
</style>