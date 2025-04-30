<template>
<div class="login-container">
  <legend>Login</legend>
  <form @submit.prevent="handleSubmit">
    <div class="form-group">
      <label for="email">Email:</label>
      <input 
        type="email" 
        id="email" 
        v-model="email" 
        required
        :class="{ 'error-input': errors.email }"
      >
      <div v-if="errors.email" class="error-message">
        {{ errors.email }}
      </div>
    </div>

    <div class="form-group">
      <label for="password">Contraseña:</label>
      <div class="password-wrapper">
        <input 
          :type="showPassword ? 'text' : 'password'" 
          id="password" 
          v-model="password" 
          required
          :class="{ 'error-input': errors.password }"
        >
        <button
          type="button"
          class="toggle-password button"
          @click="showPassword = !showPassword"
          tabindex="-1"
          aria-label="Mostrar/Ocultar contraseña"
        >
          <span class="shadow"></span>
          <span class="edge"></span>
          <span class="front">
            {{ showPassword ? 'Ocultar' : 'Mostrar' }}
          </span>
        </button>
      </div>
      <div v-if="errors.password" class="error-message">
        {{ errors.password }}
      </div>
    </div>

    <button 
      type="submit" 
      :disabled="isLoading"
      class="submit-button"
    >
      {{ isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
    </button>

    <div v-if="generalError" class="error-message">
      {{ generalError }}
    </div>
  </form>
</div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAuthStore } from '@/services/auth'
import { useRouter } from 'vue-router'
import axios from 'axios'

const showPassword = ref(false)
const authStore = useAuthStore()
const router = useRouter()

// Estado del formulario
const email = ref('')
const password = ref('')
const isLoading = ref(false)
const generalError = ref('')

const errors = computed(() => ({
  email: !email.value
    ? 'El email es requerido'
    : !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)
      ? 'El email no es valido'
      : '',
  password: password.value ? '' : 'La contraseña es requerida'
}))

const handleSubmit = async () => {
  if (Object.values(errors.value).some(error => error)) return

  isLoading.value = true
  generalError.value = ''

  try {
    // Ajusta esta URL según tu backend
    const response = await axios.post('http://127.0.0.1:5000/api/auth/login', {
      email: email.value,
      user_password: password.value
    })

    await authStore.login(response.data)
    router.push({ name: 'Home' })
  } catch (error) {
    generalError.value =
      error.response?.data?.message || error.message || 'Error de autenticación'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
:root {
  --ch-c-black: #222831;
  --ch-c-gray-dark: #393E46;
  --ch-c-yellow: #FFD369;
  --ch-c-white: #EEEEEE;
}

legend{
  text-align: center;
  font-weight: 500;
  font-size: x-large;
  padding: 20px;
  color: var(--ch-c-white);
  -webkit-text-stroke: 0.5px white
}

.login-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: var(--ch-c-gray-dark);
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.password-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.toggle-password.button {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
  padding: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  width: auto;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.toggle-password .front {
  display: block;
  position: relative;
  padding: 4px 12px;
  border-radius: 8px;
  font-size: 0.95rem;
  color: white;
  background: hsl(212, 100%, 47%);
  will-change: transform;
  transform: translateY(-2px);
  transition: transform 300ms cubic-bezier(0.3, 0.7, 0.4, 1);
}

.toggle-password .shadow,
.toggle-password .edge {
  display: none; /* Oculta los efectos grandes para hacerlo discreto */
}

.error-input {
  border-color: #ff4444;
}

.error-message {
  color: #ff4444;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

.submit-button {
  width: 100%;
  padding: 1rem;
  background-color: var(--ch-c-yellow);
  color: var(--ch-c-black);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
}

.submit-button:disabled {
  background-color: #81c784;
  cursor: not-allowed;
}
</style>