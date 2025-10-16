# EJERCICIO 2 - Operadores y estructuras

print("=== OPERADORES ===")

# Aritméticos
x = 5
y = 3
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y)
print("Resto:", x % y)
print("Potencia:", x ** y)

# Comparación
print("\nComparaciones:")
print("5 > 3:", x > y)
print("5 < 3:", x < y)
print("5 == 3:", x == y)
print("5 != 3:", x != y)

# Lógicos
print("\nLógicos:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

print("\n=== ESTRUCTURAS ===")

# If-else
numero = 10
if numero > 5:
    print("El número es mayor que 5")
else:
    print("El número es menor o igual que 5")

# For
print("\nContando del 1 al 5:")
for i in range(1, 6):
    print(i)

# While
print("\nTabla del 2:")
i = 1
while i <= 5:
    print("2 x", i, "=", 2 * i)
    i += 1

# Lista
frutas = ["manzana", "banana", "naranja"]
print("\nFrutas:")
for fruta in frutas:
    print(fruta)