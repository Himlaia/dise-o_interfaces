# ==== EJERCICIO 1 ====

# Función sin parámetros ni retorno
def funcion():
    print("Hola desde una función")

# Función con un parámetro
def saludo(nombre):
    print("Hola,", nombre)

# Función con varios parámetros
def suma(a, b):
    print(a + b)

# Función que no sabe cuántos argumentos recibirá
def numHijos(*hijos):
    print("El hijo más joven es: ", hijos[2])

# No importa el orden de la declaración si luego se usan keywords
def misHijos(hijo3, hijo2, hijo1):
    print("El hijo más joven es: " + hijo3)

# Función con valor por defecto
def origen(pais = "España"):
    print("Yo soy de " + pais)


# Función con retorno
def cuadrado(x):
    return x * x

# Función dentro de función
def funcion_externa():
    print("Esta es la función externa")
    def funcion_interna():
        print("Esta es la función interna")
    funcion_interna

# Función ya integrada
def longitud():
    lista = [1, 2, 3, 4]
    print("Longitud de la lista:", len(lista))

# Tipos de variables
varGlobal = "Esta es una variable global"

def ejVariables():
    varLocal = "Esta es una variable local"
    print(varGlobal)
    print(varLocal)

# Pruebas de funciones
funcion()
saludo("Martina")
suma(3, 4)
numHijos("Sandra", "Pepe", "Ana")
misHijos(hijo1="Nicolás", hijo2="Aixa", hijo3="Martina")
origen()
origen("Argentina")
cuadrado(3)
funcion_externa()
longitud()
ejVariables()

# ==== EJERCICIO 2 ====
def ejercicio(texto1, texto2):
    contador= 0
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            # Múltiplo de 3 y 5
            print(texto1 + " " + texto2)
        elif i % 3 == 0:
            # Múltiplo de 3
            print(texto1)
        elif i % 5 == 0:
            # Múltiplo de 5
            print(texto2)
        else:
            # No es múltiplo ni de 3 ni de 5
            print(i)
            contador += 1
    
    return contador

resultado = ejercicio("Hola", "Adiós")
print(f"\nNúmeros impresos (no textos): {resultado}")
