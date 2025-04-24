import api from "./api";

export const getBrands = async () => {
    const response = await api.get('/catalog/brand');
    return response.data.detailed.map(brand => brand.name)
};

export const getBrandsId = async (id_brand) => {
    try {
        const response = await api.get(`/catalog/brand/${id_brand}`);
        
        // Asegurarse de que response.data.detailed exista y tenga la propiedad name
        if (response.data && response.data.detailed && response.data.detailed.name) {
            return response.data.detailed.name; // Devuelve solo el nombre de la marca
        } else {
            return null; // o "" si prefieres mostrar una marca vacía
        }
    } catch (error) {
        console.error("Error al obtener la marca: ", error);
        return null;
    }
};
