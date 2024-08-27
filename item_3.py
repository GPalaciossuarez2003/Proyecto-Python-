precios = {
    "Café": 1500,
    "Té": 1000,
    "Jugo Natural": 2000,
    "Pastel de Chocolate": 2500,
    "Tarta de Frutas": 3000,
}

pedidos = {
    "Café": 1,
    "Té": 0,
    "Jugo Natural": 1,
    "Pastel de Chocolate": 1,
    "Tarta de Frutas": 2,
}

for producto, cantidad in pedidos.items():
    print(cantidad,precios[producto], cantidad * precios[producto])
