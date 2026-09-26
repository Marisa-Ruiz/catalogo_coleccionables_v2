from validations import validate_not_empty, validate_price, validate_status, validate_description

def add_piece(id, name, category, price, status, description):
    validate_not_empty(id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")
    validate_price(price)
    price = float(price)
    validate_status(status)
    validate_description(description)

    piece = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    return piece

def list_pieces(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    names = []
    for piece in catalog:
        names.append(piece['name'])

    return names

def find_piece_by_id(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    for piece in catalog:
        if piece['id'] == id:
            return piece

    return None

def remove_piece(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    try:
        piece = find_piece_by_id(catalog, id)
        if piece is None:
            raise ValueError("No se encontró ninguna pieza con ese id.")
        catalog.remove(piece)
        return True
    except ValueError:
        return False

def get_catalog_summary(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    summary = {}

    for piece in catalog:
        category = piece['category']
        if category in summary:
            summary[category] = summary[category] + 1
        else:
            summary[category] = 1

    return summary

def get_pieces_by_category(catalog, category):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    matching_names = []
    for piece in catalog:
        if piece['category'] == category:
            matching_names.append(piece['name'])

    return matching_names

def piece_exists(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")
    piece = find_piece_by_id(catalog, id)
    if piece is None:
        return False
    else:
        return True

def filter_by_status(catalog, status):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")
    validate_status(status)

    matching_pieces = []
    for piece in catalog:
        if piece['status'] == status:
            matching_pieces.append(piece)

    return matching_pieces

def filter_by_min_price(catalog, min_price):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    try:
        min_price = float(min_price)
    except ValueError:
        raise ValueError("El precio debe ser un número.")

    matching_pieces = []
    for piece in catalog:
        if piece['price'] > min_price:
            matching_pieces.append(piece)

    return matching_pieces

def get_average_price(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    if len(catalog) == 0:
        return 0

    total_price = 0
    for piece in catalog:
        total_price = total_price + piece['price']

    return total_price / len(catalog)

