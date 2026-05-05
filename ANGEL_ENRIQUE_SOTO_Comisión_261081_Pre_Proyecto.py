# LISTADO GENERAL DE PRODUCTOS EN LA TIENDA ONLINE TECHLAB
productos = [] 
continuar = True

while continuar:
    print("\n --- BIENVENIDO AL SISTEMA DE GESTIÓN DE TIENDA ONLINE TECHLAB ---")
    print("")
    print("1. Agregar un producto deseado al sistema.")
    print("2. Ver productos disponibles en el sistema.")
    print("3. Buscar producto deseado por nombre.")
    print("4. Eliminar producto del sistema.")
    print("5. Salir del programa.")
    
    opcion = input("\n -Elija una opción: ")

    if opcion == "1":
        # Guardamos en minúsculas para que la búsqueda no falle
        nombre = input("\n Nombre del producto: ").lower().strip()
        while nombre == "" or not nombre.isalpha(): 
            nombre = input("\n -Error. Ingresá el nombre de un producto valido o comprueba que no haya espacios vacios: ").lower().strip()
            
        # Validamos que el producto no se repita recorriendo la lista
        existe = False
        for p in productos:
            if p[0] == nombre:
                existe = True
        
        if existe:
            print(f"\n -Error: El producto '{nombre.capitalize()}' ya está registrado en el sistema.").lower().strip()
            continue
        # Validamos que la categoría no esté vacía y que solo contenga letras   
        categoria = input("\n Categoría del producto: ").lower().strip()       
        while categoria == "" or not categoria.isalpha():
            categoria = input("\n -Error. Ingresá la categoría del producto, la misma solo puede ser un texto: ").lower().strip()
            
        precio = input("\n Valor del producto: ")
        while not precio.isdigit():
            precio = input("\n -Error. El precio debe ser un valor numérico: ")
        # Agregamos la sublista a la lista principal
        nueva_sublista = [[nombre, categoria, int(precio)]]
        productos = productos + nueva_sublista
        print("\n -Producto agregado con éxito al sistema.")

    elif opcion == "2":
        if len(productos) == 0:
            print("\n -No hay productos guardados en el sistema.")
        else:
            print("\n --- Listado Completo ---:")
            # Usamos range para generar los índices (0, 1, 2...)
            for i in range(len(productos)):
            # i es la posición, pero para el usuario sumamos 1
                p = productos[i]
                print(f"\n -{i + 1} - {p[0].capitalize()} [{p[1].capitalize()}] ${p[2]}")

    elif opcion == "3":
        busqueda = input("\n -Producto que deseas buscar: ").lower().strip()
        encontrado = False
        # Usamos range para buscar por posición
        for i in range(len(productos)):
            if productos[i][0] == busqueda:
                p = productos[i]
                print(f"\n -Resultado: {p[0].capitalize()} - {p[1].capitalize()} - ${p[2]}")
                encontrado = True
        
        if not encontrado:
            print("\n -No se encontró el producto buscado, intente nuevamente.")

    elif opcion == "4":
        if len(productos) == 0:
            print("\n -La lista está vacía.")
        else:
            for i in range(len(productos)):
                print(f"\n -{i + 1}. {productos[i][0].capitalize()}")
            
            indice_input = input("\n -Número del producto a eliminar: ")
            
            if indice_input.isdigit():
                numero = int(indice_input)
                if 0 < numero <= len(productos):
                    posicion_a_borrar = numero - 1
                    nueva_lista = []
                    for i in range(len(productos)):
                        if i != posicion_a_borrar:
                            nueva_lista = nueva_lista + [productos[i]]
                    productos = nueva_lista
                    print("\n -Producto eliminado exitosamente.")
                else:
                    print("\n -Ese número de producto no está en la lista.")
            else:
                print("\n -Error: Debes ingresar un número de producto, no un texto.")

    elif opcion == "5":
        print("\n -Programa finalizado.")
        continuar = False
