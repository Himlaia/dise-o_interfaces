# ===== EJERCICIO 1 =====

# Asignación por valor 
a = 10
b = a
b = 20
print("Por valor -> a:", a, "b:", b)  # a no cambia

# Asignación por referencia 
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print("Por referencia -> lista1:", lista1, "lista2:", lista2)  


# ===== FUNCIONES =====
def intercambiarValor(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def intercambiarReferencia(n1, n2):
    return n2, n1


# ===== PRUEBA EJERCICIO 1 =====
num1 = 5
num2 = 10
nuevo1, nuevo2 = intercambiarValor(num1, num2)

print("\n--- Por valor (enteros) ---")
print("Originales -> num1:", num1, "num2:", num2)
print("Nuevos     -> nuevo1:", nuevo1, "nuevo2:", nuevo2)

# Variables originales
listaA = [1, 2]
listaB = [3, 4]
nuevaA, nuevaB = intercambiarReferencia(listaA, listaB)

print("\n--- Por referencia (listas) ---")
print("Originales -> listaA:", listaA, "listaB:", listaB)
print("Nuevos     -> nuevaA:", nuevaA, "nuevaB:", nuevaB)
