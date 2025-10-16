# ===== EJERCICIO =====
#   Muestra ejemplos de creación de todas las estructuras soportadas por defecto. 
#   Utiliza operaciones de inserción, borrado, actualización y ordenación.

def estructuras():
    # ===== 1. LISTAS (list) =====
    print("\n1. LISTAS (list)")
    print("-" * 30)

    # Creación
    lista = [1, 2, 3, 4, 5]
    lista_mixta = [1, "texto", 3.14, True]
    lista_vacia = []

    print(f"Lista inicial: {lista}")
    print(f"Lista mixta: {lista_mixta}")

    # Inserción
    lista.append(6)  # Al final
    print(f"Después de append(6): {lista}")

    lista.insert(2, 10)  # En posición específica
    print(f"Después de insert(2, 10): {lista}")

    lista.extend([7, 8, 9])  # Múltiples elementos
    print(f"Después de extend([7, 8, 9]): {lista}")

    # Actualización
    lista[0] = 100
    print(f"Después de lista[0] = 100: {lista}")

    # Borrado
    lista.remove(10)  # Elimina la primera ocurrencia
    print(f"Después de remove(10): {lista}")

    eliminado = lista.pop()  # Elimina y retorna el último
    print(f"Después de pop(): {lista}, elemento eliminado: {eliminado}")

    del lista[1]  # Elimina por índice
    print(f"Después de del lista[1]: {lista}")

    # Ordenación
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista desordenada: {lista_desordenada}")

    lista_ordenada = sorted(lista_desordenada)  # Nueva lista ordenada
    print(f"sorted(): {lista_ordenada}")

    lista_desordenada.sort()  # Ordena in-place
    print(f"sort() in-place: {lista_desordenada}")

    lista_desordenada.sort(reverse=True)  # Orden descendente
    print(f"sort(reverse=True): {lista_desordenada}")

    # ===== 2. TUPLAS (tuple) =====
    print("\n\n2. TUPLAS (tuple)")
    print("-" * 30)

    # Creación
    tupla = (1, 2, 3, 4, 5)
    tupla_mixta = (1, "texto", 3.14, True)
    tupla_un_elemento = (42,)  # Coma necesaria para un elemento
    tupla_vacia = ()

    print(f"Tupla inicial: {tupla}")
    print(f"Tupla mixta: {tupla_mixta}")

    # Las tuplas son inmutables, pero podemos:
    # - Acceder a elementos
    print(f"Primer elemento: {tupla[0]}")
    print(f"Último elemento: {tupla[-1]}")

    # - Crear nuevas tuplas (concatenación)
    tupla_nueva = tupla + (6, 7, 8)
    print(f"Concatenación: {tupla_nueva}")

    # - Ordenación (crear nueva tupla)
    tupla_desordenada = (64, 34, 25, 12, 22)
    tupla_ordenada = tuple(sorted(tupla_desordenada))
    print(f"Tupla original: {tupla_desordenada}")
    print(f"Tupla ordenada: {tupla_ordenada}")

    # ===== 3. CONJUNTOS (set) =====
    print("\n\n3. CONJUNTOS (set)")
    print("-" * 30)

    # Creación
    conjunto = {1, 2, 3, 4, 5}
    conjunto_mixto = {1, "texto", 3.14}  # No puede contener elementos mutables
    conjunto_vacio = set()  # No usar {} que crea diccionario vacío

    print(f"Conjunto inicial: {conjunto}")
    print(f"Conjunto mixto: {conjunto_mixto}")

    # Inserción
    conjunto.add(6)
    print(f"Después de add(6): {conjunto}")

    conjunto.update([7, 8, 9])
    print(f"Después de update([7, 8, 9]): {conjunto}")

    # Borrado
    conjunto.remove(3)  # Error si no existe
    print(f"Después de remove(3): {conjunto}")

    conjunto.discard(10)  # No error si no existe
    print(f"Después de discard(10): {conjunto}")

    eliminado = conjunto.pop()  # Elimina elemento aleatorio
    print(f"Después de pop(): {conjunto}, elemento eliminado: {eliminado}")

    # Actualización (no hay actualización directa, se elimina y agrega)
    if 2 in conjunto:
        conjunto.remove(2)
        conjunto.add(20)
    print(f"Actualización 2 -> 20: {conjunto}")

    # Ordenación
    conjunto_desordenado = {64, 34, 25, 12, 22}
    lista_ordenada_desde_set = sorted(conjunto_desordenado)
    print(f"Conjunto desordenado: {conjunto_desordenado}")
    print(f"Lista ordenada desde set: {lista_ordenada_desde_set}")

    # Operaciones de conjuntos
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(f"Set1: {set1}, Set2: {set2}")
    print(f"Unión: {set1.union(set2)}")
    print(f"Intersección: {set1.intersection(set2)}")
    print(f"Diferencia: {set1.difference(set2)}")

    # ===== 4. DICCIONARIOS (dict) =====
    print("\n\n4. DICCIONARIOS (dict)")
    print("-" * 30)

    # Creación
    diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
    diccionario_mixto = {1: "uno", "dos": 2, 3.14: "pi"}
    diccionario_vacio = {}

    print(f"Diccionario inicial: {diccionario}")
    print(f"Diccionario mixto: {diccionario_mixto}")

    # Inserción/Actualización
    diccionario["profesion"] = "Ingeniero"  # Nueva clave
    print(f"Después de agregar profesión: {diccionario}")

    diccionario.update({"telefono": "123456789", "email": "juan@email.com"})
    print(f"Después de update(): {diccionario}")

    # Actualización
    diccionario["edad"] = 31
    print(f"Después de actualizar edad: {diccionario}")

    # Borrado
    del diccionario["telefono"]
    print(f"Después de del telefono: {diccionario}")

    eliminado = diccionario.pop("email")
    print(f"Después de pop('email'): {diccionario}, valor eliminado: {eliminado}")

    # Ordenación por claves
    dict_desordenado = {"c": 3, "a": 1, "b": 2, "d": 4}
    print(f"Diccionario desordenado: {dict_desordenado}")

    # Ordenar por claves
    dict_ordenado_claves = dict(sorted(dict_desordenado.items()))
    print(f"Ordenado por claves: {dict_ordenado_claves}")

    # Ordenar por valores
    dict_ordenado_valores = dict(sorted(dict_desordenado.items(), key=lambda x: x[1]))
    print(f"Ordenado por valores: {dict_ordenado_valores}")

    # ===== 5. CADENAS (str) =====
    print("\n\n5. CADENAS (str)")
    print("-" * 30)

    # Creación
    cadena = "Hola Mundo"
    cadena_vacia = ""
    cadena_multilinea = """Esta es una
cadena de múltiples
líneas"""

    print(f"Cadena inicial: '{cadena}'")

    # Las cadenas son inmutables, pero podemos crear nuevas:
    # Inserción (concatenación)
    nueva_cadena = cadena + " Python"
    print(f"Concatenación: '{nueva_cadena}'")

    # Actualización (reemplazo)
    cadena_actualizada = cadena.replace("Mundo", "Python")
    print(f"Después de replace(): '{cadena_actualizada}'")

    # "Borrado" (reemplazo por cadena vacía)
    cadena_sin_hola = cadena.replace("Hola ", "")
    print(f"Después de 'borrar' Hola: '{cadena_sin_hola}'")

    # Ordenación de caracteres
    cadena_desordenada = "python"
    caracteres_ordenados = ''.join(sorted(cadena_desordenada))
    print(f"Cadena original: '{cadena_desordenada}'")
    print(f"Caracteres ordenados: '{caracteres_ordenados}'")

    # Operaciones con cadenas
    texto = "  Este es un ejemplo  "
    print(f"Original: '{texto}'")
    print(f"strip(): '{texto.strip()}'")
    print(f"upper(): '{texto.upper()}'")
    print(f"lower(): '{texto.lower()}'")
    print(f"split(): {texto.split()}")

    # ===== 6. RANGOS (range) =====
    print("\n\n6. RANGOS (range)")
    print("-" * 30)

    # Creación
    rango1 = range(5)  # 0 a 4
    rango2 = range(2, 8)  # 2 a 7
    rango3 = range(0, 10, 2)  # 0, 2, 4, 6, 8

    print(f"range(5): {list(rango1)}")
    print(f"range(2, 8): {list(rango2)}")
    print(f"range(0, 10, 2): {list(rango3)}")

    # Los rangos son inmutables, pero podemos convertirlos a listas para operaciones
    lista_desde_rango = list(range(10, 0, -1))  # Descendente
    print(f"range(10, 0, -1): {lista_desde_rango}")

# estructuras()  

# ==== EJERCICIO 1 ====
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.

def telefono():
    opcion = 1 

    contactos = []

    while opcion != 0:
        print("\n\n==== MENÚ ====")
        print("1. Buscar contacto")
        print("2. Añadir contacto")
        print("3. Actualizar contacto")
        print("4. Borrar contacto")
        print("0. Salir")

        opcion = int(input("Introduce una opción: "))

        match opcion:
            case 1:
                busqueda = input("Nombre a buscar: ")
                encontrado = False
                for contacto in contactos:
                    if contacto[0] == busqueda:  # contacto[0] es el nombre
                        print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")
                        encontrado = True
                if not encontrado:
                    print("Contacto no encontrado.")
            
            case 2:
                print("\n--- Añadir contacto ---")
                nombre = input("Introduce el nombre: ")
                telefono = input("Introduce el teléfono: ")
                
                # Validar teléfono
                if telefono.isdigit() and len(telefono) <= 11:
                    contactos.append([nombre, telefono])  # Añadir la lista completa
                    print("Contacto añadido correctamente")
                else:
                    print("Teléfono inválido")
                    
            case 3:
                print("\n--- Actualizar contacto ---")
                act = input("Introduce el nombre del contacto a actualizar: ")
                encontrado = False
                for contacto in contactos:
                    if contacto[0] == act:
                        nuevo_nombre = input(f"Introduce el nuevo nombre (actual: {contacto[0]}): ")
                        nuevo_telefono = input(f"Introduce el nuevo teléfono (actual: {contacto[1]}): ")
                        
                        # Validar nuevo teléfono
                        if nuevo_telefono.isdigit() and len(nuevo_telefono) <= 11:
                            contacto[0] = nuevo_nombre
                            contacto[1] = nuevo_telefono
                            print(f"Contacto actualizado. Nombre: {contacto[0]}, Teléfono: {contacto[1]}")
                        else:
                            print("Teléfono inválido. No se ha actualizado el contacto.")
                        encontrado = True
                        break
                if not encontrado:
                    print("Contacto no encontrado.")
            
            case 4: 
                print("\n--- Eliminar contacto ---")
                borrar = input("Introduce el nombre del contacto a borrar: ")
                encontrado = False
                for contacto in contactos:
                    if contacto[0] == borrar:
                        contactos.remove(contacto)
                        print(f"Contacto {borrar} eliminado correctamente.")
                        encontrado = True
                        break
                if not encontrado:
                    print("Contacto no encontrado.")

            case 0:
                print("\nSaliendo del programa...")
                break

            case _:
                print("Opción no válida. Introduce un número del 0 al 4.")
        
telefono()