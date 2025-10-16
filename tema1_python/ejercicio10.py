# EJERCICIO:
# Explora los conceptos de "decorador" y "generador", muestra cómo crearlos
# con un ejemplo genérico.

def decoradores():
    def cafe_basico():
        return "Cafe negro"

    resultado = cafe_basico()
    print(f"Pedido: {resultado}")
    print(f"Precio: $2.00")

    def con_azucar(funcion_cafe):
        def cafe_modificado():
            cafe_original = funcion_cafe()
            return cafe_original + " + azucar"
        return cafe_modificado

    # Aplicar decorador manualmente
    cafe_con_azucar = con_azucar(cafe_basico)
    resultado = cafe_con_azucar()
    print(f"Pedido: {resultado}")
    print(f"Precio: $2.50")

    # Decorador con sintaxis @
    def con_leche(funcion_cafe):
        def cafe_modificado():
            cafe_original = funcion_cafe()
            return cafe_original + " + leche"
        return cafe_modificado

    @con_leche
    def cafe_con_leche_base():
        return "Cafe negro"

    resultado = cafe_con_leche_base()
    print(f"Pedido: {resultado}")
    print(f"Precio: $3.00")

    # Multiples decoradores
    def con_crema(funcion_cafe):
        def cafe_modificado():
            cafe_original = funcion_cafe()
            return cafe_original + " + crema batida"
        return cafe_modificado

    def con_canela(funcion_cafe):
        def cafe_modificado():
            cafe_original = funcion_cafe()
            return cafe_original + " + canela"
        return cafe_modificado

    @con_canela
    @con_crema
    @con_leche
    def cafe_deluxe():
        return "Cafe negro"

    resultado = cafe_deluxe()
    print(f"Pedido: {resultado}")
    print(f"Precio: $5.50")

    # Decorador con parametros
    def con_tamaño(tamaño):
        def decorador(funcion_cafe):
            def cafe_modificado():
                cafe_original = funcion_cafe()
                return f"{tamaño} {cafe_original}"
            return cafe_modificado
        return decorador

    @con_tamaño("Grande")
    @con_leche
    def latte_grande():
        return "Cafe negro"

    resultado = latte_grande()
    print(f"Pedido: {resultado}")
    print(f"Precio: $4.00")

# decoradores()

def generadores():
    # Generador basico
    def numeros():
        yield 1
        yield 2
        yield 3
    
    gen = numeros()
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    
    # Generador infinito
    def pares():
        n = 0
        while True:
            yield n
            n += 2
    
    gen_pares = pares()
    for i in range(5):
        print(next(gen_pares))
    
    # Con for
    def impares():
        n = 1
        while n <= 10:
            yield n
            n += 2
    
    for num in impares():
        print(num)

# generadores()


# ===== EJERCICIOS ADICIONALES =====
# EJERCICIO 1:
# Crea un decorador que sea capaz de contabilizar cuántas veces
# se ha llamado a una función y aplícalo a una función de tu elección.
def contador(func):
    llamadas = 0  # variable local al decorador

    def sumar():
        nonlocal llamadas  # permite modificar la variable externa
        llamadas += 1
        print(f"Llamadas: {llamadas}")
        return func()
    
    return sumar


@contador
def saludar():
    return "Hola"

print(saludar())
print(saludar())

# EJERCICIO 2:
# Implementa un GENERADOR que produzca una secuencia numérica infinito
# de números pares de la secuencia de Fibonacci.
# Muestra cómo obtener varios valores de dicho generador utilizando
# un bucle y la función next().

def paresFibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if a % 2 == 0:
            yield a
    
gen_pares_fibonacci = paresFibonacci()
for i in range(5):
    print(next(gen_pares_fibonacci))

# EJERCICIO 3
# Crea un decorador que limite el número de valores que se pueden obtener
# de un generador. Por ejemplo, si el límite es 5, el generador debe
# detener la secuencia automáticamente tras producir 5 elementos.
#
# Aplica este decorador al generador definido en el EJERCICIO 2 y comprueba
# su funcionamiento al recorrerlo con un bucle.
# Decorador que limita el número de valores que se pueden obtener de un generador
def limite(n):
    def decorador(gen_func):
        def wrapper(*args, **kwargs):
            gen = gen_func(*args, **kwargs)
            count = 0
            while count < n:
                try:
                    yield next(gen)
                    count += 1
                except StopIteration:
                    break
        return wrapper
    return decorador

@limite(5)
def paresFibonacciLimitados():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if a % 2 == 0:
            yield a

# Probar el generador limitado
for num in paresFibonacciLimitados():
    print(num)


limite(paresFibonacci)