# ============================================================
# EJERCICIO 6: Procesamiento de ventas
# ============================================================

def calculate_discount(quantity: int, customer: str) -> float:
    """
    Calcula el descuento segun cantidad y tipo de cliente.
    - 10% si cantidad >= 10
    - 5% adicional si el cliente es 'vip'
    """
    discount = 0.0
    if quantity >= 10:
        discount += 0.10
    if customer == "vip":
        discount += 0.05
    return discount

def calculate_sale_total(sale: dict) -> float:
    """
    Calcula el total de una venta individual aplicando descuentos.
    Solo acepta ventas con status 'ok'.
    Lanza ValueError si el status no es 'ok'.
    """
    if sale["status"] != "ok":
        raise ValueError("Venta invalida: status = " + sale["status"])

    price    = sale["price"]
    quantity = sale["qty"]
    customer = sale["customer"]

    discount = calculate_discount(quantity, customer)
    subtotal = price * quantity
    subtotal = subtotal - (subtotal * discount)
    return subtotal

def calculate_total(sales: list) -> float:
    """
    Suma el total de todas las ventas validas.
    Las ventas con status distinto de 'ok' se ignoran.
    """
    total = 0.0
    for sale in sales:
        if sale["status"] == "ok":
            total += calculate_sale_total(sale)
    return total

def report_invalid_sales(sales: list) -> None:
    """Imprime las ventas que no tienen status 'ok'."""
    for sale in sales:
        if sale["status"] != "ok":
            print("Venta invalida:", sale)