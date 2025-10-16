# EJERCICIO CAFETERIA:
# En una cafetería queremos implementar un sistema de pedidos de café.
# Cada café puede tener toppings como leche, azúcar, sacarina y sabores (caramelo, chocolate, canela).
# Se pide que:

# No se pueden añadir más de 3 elementos a un café y solo puede tener un sabor:

# Cada añadido tiene un coste:

# Leche (entera o semidesnatada): 0,5 €
# Azúcar o sacarina: 0 €
# Hielo: 0,15 €

# Sabores:
# Caramelo: 0,75 €
# Chocolate: 0,5 €
# Canela: 0,25 €

# Usar decoradores para registrar cuando se añade un elemento al café
# y aplicar un descuento automático de 0,10 € cuando el café tenga exactamente 3 toppings.

# Usar un generador para preparar los cafés uno a uno, según los pedidos de los clientes.
precios_toppings = {
    "leche_entera": 0.5,
    "leche_semidesnatada": 0.5,
    "azucar": 0,
    "sacarina": 0,
    "hielo": 0.15,
    "caramelo": 0.75,
    "chocolate": 0.5,
    "canela": 0.25,
}

sabores = {"caramelo", "chocolate", "canela"}


# DECORADOR PARA REGISTRAR CUANDO SE AÑADE UN ELEMENTO
def registrar_topping(func):
    def envoltorio(self, topping):
        # Ejecutar funcion original (añadir topping)
        resultado = func(self, topping)

        # Solo mostrar mensaje si realmente se añadió el topping
        if resultado:
            # Aplicar descuento si llega a 3 toppings
            if len(self.toppings) == 3:
                self.precio = round(self.precio - 0.10, 2)
                self.mensajes.append("Descuento de 0.10€ aplicado por 3 toppings.")
            self.mensajes.append(f"'{topping}' añadido. Precio actual: {self.precio}€")
        return resultado

    return envoltorio


class Cafe:
    MAX_TOPPINGS = 3
    BASE = 1.5  # Precio base del café

    def _init_(self):
        self.toppings = []
        self.precio = Cafe.BASE
        self.tiene_sabor = False  # Para controlar que solo hay un sabor
        self.mensajes = []

    @registrar_topping
    def anadir_topping(self, topping):
        # Validar topping
        if topping not in precios_toppings:
            self.mensajes.append(f"'{topping}' no es un topping válido.")
            return False

        # Límite de toppings
        if len(self.toppings) >= Cafe.MAX_TOPPINGS:
            self.mensajes.append("no se pueden añadir más de 3 elementos.")
            return False

        # Solo un sabor permitido
        if topping in sabores:
            if self.tiene_sabor:
                self.mensajes.append("Solo se puede añadir un sabor al café.")
                return False
            self.tiene_sabor = True

        # Añadir topping y actualizar precio
        self.toppings.append(topping)
        self.precio += precios_toppings[topping]
        self.precio = round(self.precio, 2)
        return True

    def mostrar(self):
        print("\n-- Pedido de café --")
        for mensaje in self.mensajes:
            print(mensaje)
        print(f"Café con : {self.toppings} | Precio total: {self.precio}€\n")


# Generador para preparar cafés
def preparar_cafes(pedidos):
    for pedido in pedidos:
        cafe = Cafe()
        for topping in pedido.get("toppings", []):
            cafe.anadir_topping(topping)
        yield cafe  # Devuelve el café preparado


pedidos = [
    {"toppings": ["leche_entera", "azucar"]},
    {"toppings": ["leche_entera", "azucar", "caramelo"]},
]

for cafe in preparar_cafes(pedidos):
    cafe.mostrar()