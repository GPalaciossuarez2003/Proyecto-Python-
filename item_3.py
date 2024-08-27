precios = {
    "Café": 1500,
    "Té": 1000,
    "Jugo Natural": 2000,
    "Pastel de Chocolate": 2500,
    "Tarta de Frutas": 3000,
}

pedidos = {
    "Café": int(input("Ingrese la cantida de café: ")),
    "Té": int(input("Ingrese la cantida de té: ")),
    "Jugo Natural": int(input("Ingrese la cantida de Jugo Natural: ")),
    "Pastel de Chocolate": int(input("Ingrese la cantida de Pastel de Chocolate: ")),
    "Tarta de Frutas": int(input("Ingrese la cantida de Tarta de Frutas: ")),
}
total = 0
for producto, cantidad in pedidos.items():
    total += cantidad * precios[producto]

print(total)