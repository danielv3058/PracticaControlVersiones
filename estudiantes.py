nombre = input("Nombre: ")
edad = int(input("Edad: "))
carrera = input("Carrera: ")
print("\nDATOS DEL ESTUDIANTE")
print("Nombre:", nombre)
print("Edad:", edad)
print("Carrera:", carrera)
if edad >= 18:
    print("Estudiante mayor de edad")
else:
    print("Estudiante menor de edad")