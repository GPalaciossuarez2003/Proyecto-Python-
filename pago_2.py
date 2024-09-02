#Solicitar ingreso al usuario
precio = int(input("Ingrese el precio del producto: "))
monto = int(input("Ingrese el monto con el que pago: "))
#Realizar Calculo
total = monto - precio

#Calcular cuantos billetes de 1000 se requieren
billetes_mil= int(total / 1000)
monedas = billetes_mil*total/500

#Mostrar el resultado 
print(f"El vuelto es de {total}")
print(f"El vuelto en billetes de $1000 deben ser: {billetes_mil}")
print(f"El vuelto en monedas de $500 deben ser: {}")
