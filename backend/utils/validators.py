from models.brand import brand_exists
from models.type_product import type_product_exists


def validate_product_data(data, for_update=False):
    required_fields = [
        "name",
        "description",
        "price",
        "stock",
        "id_brand",
        "id_type_product",
    ]

    if not for_update:
        # Verify all fields are present
        missing = [field for field in required_fields if field not in data]
        if missing:
            return False, f"Fields missing: {', '.join(missing)}"

    # Validate required field are not empty (if exist)
    if any(not str(data[field]).strip() for field in ["name", "description"]):
        return False, "Name and description are required fields"

    # Validate numbers type (if exist)
    try:
        if "price" in data:
            data["price"] = float(data["price"])
        if "stock" in data:
            data["stock"] = int(data["stock"])
        if "id_brand" in data:
            data["id_brand"] = int(data["id_brand"])
        if "id_type_product" in data:
            data["id_type_product"] = int(data["id_type_product"])
    except ValueError:
        return False, "Tipos de datos inválidos"

    # Verify if relation exist (only if data exist)
    if not brand_exists(data["id_brand"]):
        return False, "Brand not found"

    if not type_product_exists(data["id_type_product"]):
        return False, "type product not found"

    return True, data
