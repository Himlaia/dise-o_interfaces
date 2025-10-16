# EJERCICIO:
# Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
# atributos y una función que los imprima.
# Una vez implementada, instancia, establece sus parámetros, modifícalos e imprímelos
# utilizando su función.
# Explora los métodos de instancia, clase y estáticos, pon un ejemplo de cada uno de ellos

class Perro:
    # Atributo de clase (Atributo estático)
    especie = "Canis"

    def __init__(self, nombre, raza): # Constructor
        # Atributos de instancia (Atributo de objeto)
        self.nombre = nombre
        self.raza = raza

        print(f"Has adoptado al perro {nombre} de raza {raza}")

    # Método de instancia (Método nonstatic, .this)
    def mostrar_info(self): 
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Especie: {Perro.especie}")

    # Método de clase (Método estático que usa la clase)
    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie
        print(f"La nueva especie ahora es: {cls.especie}")

    # Método estático
    @staticmethod
    def ladrar():
        print("¡Guau, guau!")


# Instanciación de objetos (Creación de objetos)
perro1 = Perro("Max", "Bulldog")
perro2 = Perro("Dana", "Beagle")

# Llamada a método de instancia (objeto.metodo)
perro1.mostrar_info()
perro2.mostrar_info()

# Modificación de atributos de instancia (objeto.atributo = valor)
perro1.nombre = "Rocky"
perro1.raza = "Boxer"

# Llamada a método de instancia tras modificacion
perro1.mostrar_info()

# Llamada a método de clase (Clase.metodo())
Perro.cambiar_especie("Canis familiaris")

# Llamada a método estático
Perro.ladrar()

# EJERCICIO 1:
# Implementa dos clases que representen las estructuras de Pila y Cola.
# Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
# retornar el número de elementos e imprimir todo su contenido.
# Además, cada clase debe incluir al menos:
# - Un *método de instancia* para gestionar elementos.
# - Un *método de clase*, por ejemplo, para contar cuántas instancias se han creado
#   o modificar un atributo compartido por todas las pilas/colas.
# - Un *método estático*, por ejemplo, para validar elementos antes de añadirlos
#   o realizar alguna comprobación auxiliar que no dependa de la instancia.
# Finalmente, crea varias instancias de cada clase y prueba todos los métodos
# mostrando los resultados por pantalla.

class Pila: # Stack (LIFO)
    contador_pilas = 0

    def __init__(self):
        self.lista = []
        Pila.contador_pilas += 1

    def push(self, añadir):
        if Pila.validar_elemento(añadir):
            self.lista.append(añadir)
            print("Contenido añadido correctamente.")
        else:
            print("El contenido no es válido. Inténtelo de nuevo.")

    def pop(self):
        elemento = self.lista.pop()
        print("Contenido eliminado correctamente.")
        return elemento

    def size(self):
        return print("Tamaño:", len(self.lista))

    def mostrar_info(self):
        print(f"Contenido: {self.lista}")

    @classmethod
    def contar_instancias(cls):
        return cls.contador_pilas

    @staticmethod
    def validar_elemento(elemento):
        if elemento is not None:
            return True
        else:
            return False

class Cola: # Queue (FIFO)
    contador_colas = 0

    def __init__(self):
        self.lista = []
        Cola.contador_colas += 1

    def enqueue(self, añadir):
        if Cola.validar_elemento(añadir):
            self.lista.append(añadir)
            print("Contenido añadido correctamente.")
        else:
            print("El contenido no es válido. Inténtelo de nuevo.")

    def dequeue(self):
        elemento = self.lista.pop(0)
        print("Contenido eliminado correctamente.")
        return elemento

    def size(self):
        return print("Tamaño:", len(self.lista))

    def mostrar_info(self):
        print(f"Contenido: {self.lista}")

    @classmethod
    def contar_instancias(cls):
        return cls.contador_colas

    @staticmethod
    def validar_elemento(elemento):
        if elemento is not None:
            return True
        else:
            return False

# Pruebas Pila
pila1 = Pila()
pila1.push("A")
pila1.push("B")
pila1.push("C")
pila1.mostrar_info()
pila1.size()
pila1.pop()
pila1.mostrar_info()

# Pruebas Cola
cola1 = Cola()
cola1.enqueue("A")
cola1.enqueue("B")
cola1.enqueue("C")
cola1.mostrar_info()
cola1.size()
cola1.dequeue()
cola1.mostrar_info()