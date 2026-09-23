def validate_not_empty(value, field_name):
    if value.strip() == "":
        raise ValueError(f"El campo {field_name} no puede estar vacío.")

def validate_price(price):
    try:
        price_number = float(price)
    except ValueError:
        raise ValueError("El precio debe ser un número.")
    if price_number <= 0:
        raise ValueError("El precio debe ser mayor que 0.")

def validate_status(status):
    if status not in ["disponible", "reservada", "vendida"]:
        raise ValueError("El estado debe ser disponible, reservada o vendida.")


def validate_description(description):
    if not ("usada" in description or "certificada" in description):
        raise ValueError("La descripción debe incluir 'usada' o 'certificada'.")