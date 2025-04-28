<template>
<div class="registro-wrapper">
  <form @submit.prevent="handleSubmit" class="registro-form">
    <div id="logo">
        <img src="../../assets/img/logo.jpeg" alt="Logo">
    </div>
    <h1>Registro de Usuario</h1>
    <p>Por favor, completa el siguiente formulario para registrarte.</p>
    <div class="form-group">
      <label for="name">Nombre</label>
      <input id="name" v-model="form.username" type="text" required />
    </div>

    <div class="form-group">
      <label for="email">Correo electrónico</label>
      <input id="email" v-model="form.email" type="email" required />
    </div>

    <div class="form-group">
        <label for="password">Contraseña</label>
        <div class="password-input-group">
          <input 
            id="password" 
            v-model="form.user_password" 
            :type="showPassword ? 'text' : 'password'" 
            required 
            @input="validatePasswords"
          />
          <button 
            type="button" 
            class="show-password-btn"
            @click="toggleShowPassword"
            v-if="passwordError"
          >
            {{ showPassword ? 'Ocultar' : 'Mostrar' }}
          </button>
        </div>
        <div v-if="passwordError" class="error-message">
          {{ passwordError }}
        </div>
      </div>
      <div class="form-group">
        <label for="password-confirm">Confirmación de Contraseña</label>
        <div class="password-input-group">
          <input 
            id="password-confirm" 
            v-model="form.user_password2" 
            :type="showPassword ? 'text' : 'password'" 
            required 
            @input="validatePasswords"
          />
          <button 
            type="button" 
            class="show-password-btn"
            @click="toggleShowPassword"
            v-if="passwordError"
          >
            {{ showPassword ? 'Ocultar' : 'Mostrar' }}
          </button>
        </div>
        <div v-if="passwordError" class="error-message">
          {{ passwordError }}
        </div>
      </div>

    <button id="btn-registrar" type="submit" :disabled="isLoading">Registrar</button>

    <!-- Mensajes -->
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </form>
</div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { registerUser } from '@/services/authService'

const form = ref({
  username: '',
  user_password: '',
  user_password2: '', // Agregado para la confirmación
  email: '',
})

const passwordError = ref('')
const isLoading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')
const showPassword = ref(false)
const toggleShowPassword = () => {
  showPassword.value = !showPassword.value
}

const validatePasswords = () => {
  if (form.value.user_password === '') {
    passwordError.value = 'La contraseña es requerida'
    return
  }

  if (form.value.user_password.length < 8) {
    passwordError.value = 'La contraseña debe tener al menos 8 caracteres'
    return
  }

  if (form.value.user_password2 === '') {
    passwordError.value = 'La confirmación es requerida'
    return
  }

  if (form.value.user_password !== form.value.user_password2) {
    passwordError.value = 'Las contraseñas no coinciden'
    return
  }

  passwordError.value = ''
}

const arePasswordsValid = computed(() => {
  return form.value.user_password === form.value.user_password2 &&
         form.value.user_password.length >= 8 &&
         passwordError.value === ''
})

const handleSubmit = async () => {
  if (!arePasswordsValid.value) {
    passwordError.value = 'Por favor, revise las contraseñas'
    return
  }

  try {
    isLoading.value = true
    const response = await registerUser(form.value)
    successMessage.value = 'Registro exitoso'
    errorMessage.value = ''
    form.value = { 
      username: '', 
      user_password: '', 
      user_password2: '', 
      email: '' 
    }
    setTimeout(() => (successMessage.value = ''), 3000)
  } catch (error) {
    successMessage.value = ''
    errorMessage.value = error.response?.data?.message || 'Error al registrar usuario'
  } finally {
    isLoading.value = false
  }
}
</script>

<style src="../../assets/css/authl/Register.css"></style>
