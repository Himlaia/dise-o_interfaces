# EJERCICIO:
# Explora el concepto de manejo de excepciones.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.

a = 5; b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("No se puede dividir por 0.")

# EJERCICIO 1:
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado.

# Excepción personalizada
class CustomError(Exception):
    pass

def process_data(data, divisor, index):
    """Función que puede lanzar 3 tipos de excepciones diferentes"""
    if data is None:
        raise CustomError("Los datos no pueden ser None")
    
    # Puede lanzar ZeroDivisionError
    result = data / divisor
    
    # Puede lanzar IndexError
    my_list = [1, 2, 3]
    value = my_list[index]
    
    return result, value

# Llamada a la función con manejo de excepciones
try:
    result = process_data(10, 2, 1)  # Caso exitoso
    print(f"Resultado: {result}")
except CustomError as e:
    print(f"Error personalizado: {type(e).__name__} - {e}")
except ZeroDivisionError as e:
    print(f"Error de división: {type(e).__name__} - {e}")
except IndexError as e:
    print(f"Error de índice: {type(e).__name__} - {e}")
except Exception as e:
    print(f"Error inesperado: {type(e).__name__} - {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("La ejecución ha finalizado.")

