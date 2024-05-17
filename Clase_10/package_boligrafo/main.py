from class_boligrafo import * 

print("\nBuenos dias, vamos a configurar su boligrafo digital.\n")
boligrafo_1 = Boligrafo(input("Ingrese el color del bolígrafo (rojo/verde/azul): "),
                        input("Ingrese el grosor del bolígrafo (fino/grueso): "))

texto_a_escribir = input("Ingrese el texto que desea escribir: ")
print(boligrafo_1.escribir(texto_a_escribir))
while True:
    continuar = input("Desea ingresar otro texto si/no : ")
    if continuar == "si": 
        texto_a_escribir = input("Ingrese el texto que desea escribir: ")
        print(boligrafo_1.escribir(texto_a_escribir))
    else: 
        break


recargar_lapicera = input("¿Desea recargar la lapicera? (si/no): ")
if recargar_lapicera.lower() == "si":
    cantidad_tinta = input("Ingrese la cantidad de tinta a recargar: ")
    print(boligrafo_1.recargar(cantidad_tinta))
  