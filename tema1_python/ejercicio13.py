# EJERCICIO:
# Explora los principios fundamentales de la Programación Orientada a Objetos (POO),
# incluyendo los conceptos de herencia, polimorfismo, encapsulamiento, cohesión,
# acoplamiento y abstracción, mediante los siguientes ejemplos:

# EJERCICIO 1:
# Crea una superclase llamada "Animal" que represente de forma general a los animales.
# Esta clase debe incluir un método llamado "hacer_sonido" que deberá ser redefinido
# por las subclases.

# Implementa dos subclases:
# - "Perro", que herede de "Animal" y emita el sonido "Guau".
# - "Gato", que herede de "Animal" y emita el sonido "Miau".

# Por último, crea una función que reciba una lista de animales y, utilizando
# polimorfismo, imprima el sonido que emite cada uno.

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

def lista_animales(animales):
    for animal in animales:
        print(animal.hacer_sonido())  

# Ejemplo de uso:
perro1 = Perro("Canino", 3)
gato1 = Gato("Felino", 2)
perro2 = Perro("Canino", 5)

mis_animales = [perro1, gato1, perro2]

print("=== Sonidos de los animales ===")
lista_animales(mis_animales)

# EJERCICIO 2:
# Implementa la jerarquía de una empresa de desarrollo de software, formada por
# una superclase "Empleado" y las siguientes subclases:
# - "Gerente"
# - "GerenteDeProyecto"
# - "Programador"

# Cada empleado debe tener un identificador y un nombre.
# Dependiendo de su rol, cada tipo de empleado tendrá propiedades y funciones
# exclusivas de su actividad, y los gerentes deberán almacenar los empleados
# que tienen a su cargo.

# Aplicar los conceptos de abstracción, encapsulamiento, cohesión y bajo acoplamiento.

from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    def funciones(self):
        return "Trabajar"
    
    @abstractmethod
    def mostrar_info_empleado(self):
        pass

    @property # Getter
    def nombre(self):
        return self._nombre
    
    @nombre.setter # Setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

class Gerente(Empleado):
    def __init__(self, id, nombre, empleados_a_cargo=None):
        super().__init__(id, nombre)
        self._empleados_a_cargo = empleados_a_cargo
       
        empleados_a_cargo if self._empleados_a_cargo == empleados_a_cargo else self._empleados_a_cargo = []

    def funciones(self):
        return "Dirigir empleados"

    def mostrar_info_empleado(self):
        return f"Gerente: {self._nombre} (ID: {self._id}), Empleados a cargo: {len(self._empleados_a_cargo)}"
        
    @property
    def empleados_a_cargo(self):
        return self._empleados_a_cargo
        
    @empleados_a_cargo.setter
    def empleados_a_cargo(self, nuevos_empleados):
        if isinstance(nuevos_empleados, list):
            self._empleados_a_cargo = nuevos_empleados
        else:
            raise ValueError("Los empleados a cargo deben ser una lista.")

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self._empleados_a_cargo.append(empleado)
        else:
            raise ValueError("Solo se pueden agregar objetos de tipo Empleado.")

    def remover_empleado(self, empleado):
        if empleado in self._empleados_a_cargo:
            self._empleados_a_cargo.remove(empleado)

class GerenteDeProyecto(Gerente):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def funciones(self):
        return "Dirigir proyectos"

    def mostrar_info_empleado(self):
        return f"Gerente de Proyecto: {self._nombre} (ID: {self._id})"
        
    @property
    def empleados_a_cargo(self):
        return self._empleados_a_cargo
        
    @empleados_a_cargo.setter
    def empleados_a_cargo(self, nuevos_empleados):
        if isinstance(nuevos_empleados, list):
            self._empleados_a_cargo = nuevos_empleados
        else:
            raise ValueError("Los empleados a cargo deben ser una lista.")

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self._empleados_a_cargo.append(empleado)
        else:
            raise ValueError("Solo se pueden agregar objetos de tipo Empleado.")

    def remover_empleado(self, empleado):
        if empleado in self._empleados_a_cargo:
            self._empleados_a_cargo.remove(empleado)

    def mostrar_info_empleado(self):
        return f"Gerente: {self._nombre} (ID: {self._id}), Empleados a cargo: {len(self._empleados_a_cargo)}"

class Programador(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def funciones(self):
        return "Programar"
