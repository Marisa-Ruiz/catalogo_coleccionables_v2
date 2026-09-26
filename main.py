from catalog import add_piece, list_pieces, find_piece_by_id, remove_piece, filter_by_status, get_average_price

catalog = []

print("======================================")
print("BIENVENIDO AL SISTEMA DE CATÁLOGO V2.0")
print("======================================")

running = True
while running:
    print("\n--- MENÚ ---")
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar pieza por id")
    print("6. Eliminar una pieza")
    print("7. Salir")

    option = input("Elige una opción (1-7): ")

    if option == "1":
        item_id = input("Introduce el ID de la pieza: ")
        name = input("Introduce tu nombre de la pieza: ")
        category = input("Introduce la categoría de la pieza: ")
        price = input("Introduce la precio de la pieza: ")
        status = input("Introduce la status a la pieza (disponible/resevada/vendida): ")
        description = input("Introduce la descripción de la pieza (debe incluir 'usada' o 'certificada'): ")

        try:
            new_piece = add_piece(item_id, name, category, price, status, description)
            catalog.append(new_piece)
            print("\nPieza registrada correctamente.")
        except ValueError as e:
            print(f"\nError al registrar la pieza: {e}")

    elif option == "2":
        if len(catalog) == 0:
            print("\nEl catálogo está vacío.")
        else:
            for piece in catalog:
                print(f"\nID: {piece['id']}")
                print(f"Nombre: {piece['name']}")
                print(f"Categoria: {piece['category']}")
                print(f"Precio: {piece['price']}")
                print(f"Estado: {piece['status']}")
                print(f"Descripción: {piece['description']}")

    elif option == "3":
        available_pieces = filter_by_status(catalog, "disponible")
        if len(available_pieces) == 0:
            print("\nNo hay piezas disponibles.")
        else:
            for piece in available_pieces:
                print(f"ID: {piece['id']}")
                print(f"Nombre: {piece['name']}")
                print(f"Categoria: {piece['category']}")
                print(f"Precio: {piece['price']}")
                print(f"Estado: {piece['status']}")
                print(f"Descripcion: {piece['description']}")
    elif option == "4":
        average = get_average_price(catalog)
        print(f"\nEL precio promedio del catálogo es: {average: .2f}")

    elif option == "5":
        search_id = input("Introduce el ID de la pieza a buscar: ")
        piece = find_piece_by_id(catalog, search_id)
        if piece is None:
            print("\nNo se encontró ninguna pieza con ese id.")
        else:
            print(f"ID: {piece['id']}")
            print(f"Nombre: {piece['name']}")
            print(f"Categoria: {piece['category']}")
            print(f"Precio: {piece['price']}")
            print(f"Estado: {piece['status']}")
            print(f"Descripcion: {piece['description']}")

    elif option == "6":
        delete_id = input("Introduce el ID de la pieza a eliminar:")
        removed = remove_piece(catalog, delete_id)
        if removed:
            print("\nPieza eliminada correctamente.")
        else:
            print("\nNo  se encontró ninguna pieza con ese id.")

    elif option == "7":
        print("\n¡Gracias por usar el sistema de catálogo! Hasta pronto.")
        running = False
    else:
        print("\nOpción no válida. Introduce un número entre 1 y 7.")
