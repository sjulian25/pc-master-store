import api from "./api";

export const getBrands = async () => {
    const response = await api.get('/catalog/brand');
    return response.data.detailed.map(brand => brand.name)
};  