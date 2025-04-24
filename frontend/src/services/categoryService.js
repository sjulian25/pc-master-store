import api from "./api";

export const getCategory = async () => {
    const response = await api.get('/catalog/category');
    return response.data.detail.map(category => category.name)
}
