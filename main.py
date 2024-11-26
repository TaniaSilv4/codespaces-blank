
 #lee la variable, le asigna un valor y la guardia en memoria

nombre = input("Ingresa tu nombre: ") #imprime un mensaje al usuario y espera a que ingrese un dato
apellido = input("Ingresa tu apellido : ") 
ciudad = input("¿En que ciudad vives?: ") 
nombre_completo = f"{nombre} {apellido}"
print(f"Nombre completo: {nombre_completo}")
print(f"Hola, {nombre} {apellido}. quien vive en: {ciudad}. Puedes consultar")

def sumar(x, y):
    return x + y
#solicitar que el usuario que ingrese dos numeros
numero1 = float(input("introduce el primer numero: "))
numero2 = float(input("introduce el segundo numero:"))
#calcular la suma
resultado = sumar(numero1, numero2)
#mostrar resultado
print(f"tu resultado: {resultado}" )