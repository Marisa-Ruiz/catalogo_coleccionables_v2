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
    pass
elif option == "2":
    pass
elif option == "3":
    pass
elif option == "4":
    pass
elif option == "5":
    pass
elif option == "6":
    pass
elif option == "7":
    print("\n¡Gracias por usar el sistema de catálogo! Hasta pronto.")
    running = False
else:
    print("\nOpción no válida. Introduce un número entre 1 y 7.")
