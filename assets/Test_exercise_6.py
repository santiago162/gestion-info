from exercise6 import calculate_sale_total, calculate_total


def test_sin_descuento():
    sale = {"status": "ok", "price": 100.0, "qty": 1, "customer": "regular"}
    assert calculate_sale_total(sale) == 100.0

def test_descuento_por_cantidad():
    sale = {"status": "ok", "price": 100.0, "qty": 10, "customer": "regular"}
    assert calculate_sale_total(sale) == 900.0

def test_descuento_vip():
    sale = {"status": "ok", "price": 100.0, "qty": 1, "customer": "vip"}
    assert calculate_sale_total(sale) == 95.0

def test_descuento_combinado():
    sale = {"status": "ok", "price": 100.0, "qty": 10, "customer": "vip"}
    assert calculate_sale_total(sale) == 850.0

def test_venta_invalida_lanza_excepcion():
    sale = {"status": "error", "price": 100.0, "qty": 1, "customer": "regular"}
    try:
        calculate_sale_total(sale)
        assert False, "Debia lanzar ValueError"
    except ValueError:
        pass

def test_total_ignora_ventas_invalidas():
    ventas = [
        {"status": "ok",    "price": 200.0, "qty": 1,  "customer": "regular"},
        {"status": "error", "price": 999.0, "qty": 99, "customer": "vip"},
        {"status": "ok",    "price": 100.0, "qty": 10, "customer": "vip"},
    ]
    assert calculate_total(ventas) == 1050.0