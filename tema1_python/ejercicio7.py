# ==== EJERCICIO 1 ====
print("\n\nEJERCICIO PRINCIPAL: Numeros del 100 al 0")
print("-" * 50)

def imprimir_numeros_recursivo(numero):
    if numero < 0:
        return
    print(numero)
        
    imprimir_numeros_recursivo(numero - 1)

print("Imprimiendo numeros del 100 al 0 usando recursion:")


imprimir_numeros_recursivo(100)

# ==== EJERCICIO EXTRA ====
def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El factorial no esta definido para numeros negativos")
    
    # CASO BASE: 0! = 1 y 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # CASO RECURSIVO: n! = n x (n-1)!
    return n * factorial_recursivo(n - 1)

# Ejemplos de factorial
print("Ejemplos de factorial:")
for i in range(6):
    resultado = factorial_recursivo(i)
    print(f"{i}! = {resultado}")

print(f"\n10! = {factorial_recursivo(10):,}")

# ===== EJERCICIO EXTRA 2 =====
def fibonacci_recursivo(posicion):
    
    if posicion < 0:
        raise ValueError("La posicion debe ser un numero no negativo")
    
    # CASOS BASE
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    
    # CASO RECURSIVO: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

# Ejemplo de Fibonacci
print("Primeros numeros de la sucesion de Fibonacci:")
for i in range(15):
    valor = fibonacci_recursivo(i)
    print(f"F({i}) = {valor}")
