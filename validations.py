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
    normalized = status.lower()
    valid_statuses = status.lower()
    if normalized not in valid_statuses:
        raise ValueError("El estado debe ser disponible, reservada o vendida.")

def validate_description(description):
    lowered = description.lower()
    if not ("usad" in lowered or "certificad" in lowered):
        raise ValueError("La descripción debe incluir 'usada' o 'certificada'.")