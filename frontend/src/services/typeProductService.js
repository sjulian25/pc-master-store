import api from "./api";

export const getAllTypeProduct = async () => {
    try {
      const response = await api.get("/catalog/type_products");
      return response.data;
    } catch (error) {
      console.error("Error al obtener los tipos de producto:", error);
      return []; // O podrías lanzar el error: throw error
    }
  };
