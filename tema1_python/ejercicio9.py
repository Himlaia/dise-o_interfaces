# ==== EJERCICIO ====
def ejercicio():
    # STACKS
    stack = []

    # Push / Añadir
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print("Stack: ", stack)

    # Peek / Mirar cuál es el elemento sin borrar
    elementoArriba = stack[-1]
    print("Peek: ", elementoArriba)

    # Pop / Muestra el último elenmento y lo borra
    elementoEliminado = stack.pop()
    print("Pop: ", elementoEliminado)

    # Stack después de pop
    print("Stack actual: ", stack)

    # Size / Tamaño
    print("Tamaño: ", len(stack))

    # QUEUES
    queue = []

    # Enqueue / Añadir
    queue.append('1')
    queue.append('2')
    queue.append('3')
    print("Queue: ", queue)

    # Peek
    elementoFrente = queue[0]
    print("Peek: ", elementoFrente)

    # Dequeue / Quita y devuelve el primer elemento de la cola
    elementoEliminado = queue.pop(0)
    print("Dequeue: ", elementoEliminado)

    # Queue después de pop
    print("Queue después de Dequeue: ", queue)

    # Size
    print("Tamaño: ", len(queue))

# ==== EJERCICIO 1 ====
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
# de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
# que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
# Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
# el nombre de una nueva web.
# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
# impresora compartida que recibe documentos y los imprime cuando así se le indica.
# La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
# interpretan como nombres de documentos.

def ejercicio_navegador_web():
    """Simulador de navegador web usando stacks"""
    print("\n" + "=" * 60)
    print("EJERCICIO 1A: SIMULADOR DE NAVEGADOR WEB (usando Stack)")
    print("=" * 60)
    
    # Variables para simular el navegador (usando listas como stacks)
    historial_atras = []      # Stack para paginas anteriores
    historial_adelante = []   # Stack para paginas futuras (cuando vamos atras)
    pagina_actual = None      # Pagina donde estamos ahora
    
    print("Bienvenido al Simulador de Navegador Web!")
    print("Comandos:")
    print("  - 'atras' o 'atrás': Ir a la pagina anterior")
    print("  - 'adelante': Ir a la pagina siguiente") 
    print("  - 'estado': Mostrar estado del navegador")
    print("  - 'salir': Terminar simulacion")
    print("  - Cualquier otra palabra: Navegar a esa pagina\n")
    
    while True:
        comando = input("> ").strip()
        
        if comando.lower() == "salir":
            print("Cerrando navegador...")
            break
            
        elif comando.lower() in ["atras", "atrás"]:
            # Ir atras en el historial
            if not historial_atras:
                print("No hay paginas anteriores en el historial")
            else:
                # Mover pagina actual al historial "adelante"
                if pagina_actual:
                    historial_adelante.append(pagina_actual)
                
                # Obtener la pagina anterior (pop del stack)
                pagina_actual = historial_atras.pop()
                print(f"Yendo atras a: {pagina_actual}")
                
        elif comando.lower() == "adelante":
            # Ir adelante en el historial
            if not historial_adelante:
                print("No hay paginas futuras en el historial")
            else:
                # Mover pagina actual al historial "atras"
                if pagina_actual:
                    historial_atras.append(pagina_actual)
                
                # Obtener la pagina siguiente (pop del stack)
                pagina_actual = historial_adelante.pop()
                print(f"Yendo adelante a: {pagina_actual}")
                
        elif comando.lower() == "estado":
            # Mostrar estado actual del navegador
            print(f"Pagina actual: {pagina_actual if pagina_actual else 'Ninguna'}")
            print(f"Historial atras: {historial_atras}")
            print(f"Historial adelante: {historial_adelante}")
            
        elif comando:  # Si no esta vacio
            # Navegar a una nueva pagina
            if pagina_actual:
                # Guardar la pagina actual en el historial (push al stack)
                historial_atras.append(pagina_actual)
            
            # Al navegar a una nueva pagina, perdemos el historial "adelante"
            historial_adelante.clear()
            
            pagina_actual = comando
            print(f"Navegando a: {pagina_actual}")
            
        else:
            print("Comando vacio. Introduce una pagina web o comando.")

def ejercicio_impresora_compartida():
    """Simulador de impresora compartida usando queues"""
    print("\n" + "=" * 60)
    print("EJERCICIO 1B: SIMULADOR DE IMPRESORA COMPARTIDA (usando Queue)")
    print("=" * 60)
    
    # Variables para simular la impresora (usando lista como queue)
    cola_impresion = []  # Queue para documentos pendientes
    documentos_impresos = 0
    
    print("Bienvenido al Simulador de Impresora Compartida!")
    print("Comandos:")
    print("  - 'imprimir': Imprimir el siguiente documento de la cola")
    print("  - 'cola': Mostrar estado de la cola")
    print("  - 'salir': Terminar simulacion")
    print("  - Cualquier otra palabra: Agregar documento a la cola\n")
    
    while True:
        comando = input("> ").strip()
        
        if comando.lower() == "salir":
            print("Cerrando impresora...")
            break
            
        elif comando.lower() == "imprimir":
            # Imprimir siguiente documento en la cola
            if not cola_impresion:
                print("No hay documentos en la cola de impresion")
            else:
                # Quitar el primer documento (FIFO - First In, First Out)
                documento = cola_impresion.pop(0)
                documentos_impresos += 1
                print(f"Imprimiendo: '{documento}'")
                print(f"Documento '{documento}' impreso correctamente")
                print(f"Documentos restantes en cola: {len(cola_impresion)}")
                
        elif comando.lower() == "cola":
            # Mostrar estado actual de la cola
            if not cola_impresion:
                print("La cola de impresion esta vacia")
            else:
                print(f"Cola de impresion ({len(cola_impresion)} documentos):")
                for i, doc in enumerate(cola_impresion, 1):
                    print(f"   {i}. {doc}")
            print(f"Total documentos impresos: {documentos_impresos}")
            
        elif comando:  # Si no esta vacio
            # Agregar documento a la cola
            cola_impresion.append(comando)  # Agregar al final (enqueue)
            print(f"Documento '{comando}' agregado a la cola")
            print(f"Documentos en cola: {len(cola_impresion)}")
            
        else:
            print("Comando vacio. Introduce un nombre de documento o comando.")

# ===== LLAMADAS A LOS EJERCICIOS =====
# Descomenta la linea del ejercicio que quieras ejecutar:

ejercicio_navegador_web()
# ejercicio_impresora_compartida()