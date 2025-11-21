texto = input("Introduce un texto: ")
palabra =input("Introduce una palabra a buscar: ")

palabras = texto.split(" ")
contador = 0
for p in palabras:
    if p == palabra:
        contador = contador + 1

print(f"La palabra {palabra} aparece {contador} veces")