#PARCIAL

#1. Suma de pares positivos

i=5
c=0
d=0
while i>0:    #Se toma el while para que pregunte solo 5 veces por un número
    a=int(input("Ingrese un número "))
    i=i-1     
    b=a%2     #Nos dice si el número es para al dar un residuo cero
    if (a>0) and (b==0):   #Verifica que se cumplan las dos condiciones de que sea par y además sea positivo
        d=c+a   #Efectua la operación a medida que se van dando los números     
    c=d        #La variable c tiene la función de almacenar el valor de cada una de las sumas de los números que se van proporcionando
print(f"La suma de los números pares positivos es: {d}")


#2. Clasificación de la edad

g=int(input("Ingrese su edad: "))
#El if y los elif dan los parametros para determinar a que rango de edad pertenece
if 0<g<13:
    print("Niño")
elif 13<=g<=17:
    print("Adolescente")
elif 18<=g<=59:
    print("Adulto")
elif 60<=g:
    print("Adulto mayor")
else :
    print("Usted digito un número inválida")


#3. Contador de vocales

h=input("Ingrese un texto: ")
i=h.lower()       #Tiene la función de volver todo minúsculas para evitar errores
#Las siguientes 5 líneas sirven para contar cada una de las vocales
j=i.count("a")    
k=i.count("e")
m=i.count("i")
n=i.count("o")
o=i.count("u")
print(f"El texto cuenta con \n a : {j} \n e : {k} \n i : {m} \n o : {n} \n u : {o}")
