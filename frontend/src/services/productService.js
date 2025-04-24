import api from './api'

export const getProductById = async (id) => {
const response = await api.get(`/catalog/products/${id}`)
return response.data
}