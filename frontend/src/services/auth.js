import { defineStore } from 'pinia'

const storedUser = localStorage.getItem('user')
export const useAuthStore = defineStore('auth', {
    state: () => ({
    user: storedUser && storedUser !== "undefined" ? JSON.parse(storedUser) : null,
    isLoggedIn: localStorage.getItem('isLoggedIn') === 'true'
    }),
    actions: {
    login(userData) {
        this.user = userData
        this.isLoggedIn = true
        localStorage.setItem('user', JSON.stringify(userData))
        localStorage.setItem('isLoggedIn', 'true')
    },
    logout() {
        this.user = null
        this.isLoggedIn = false
        localStorage.removeItem('user')
        localStorage.removeItem('isLoggedIn')
    }
    }
})