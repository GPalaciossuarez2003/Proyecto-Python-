#Solicitar ingreso al usuario
precio = int(input("Ingrese el precio del producto: "))
monto = int(input("Ingrese el monto con el que pago: "))
#Realizar Calculo
total = monto - precio
#Mostrar el resultado 
print(f"El vuelto es de {total}")