import numpy as np
import json

def only_letra_numeros(cadena, tipo):
    if tipo == 'letras':
        return cadena.isalpha()
    elif tipo == 'numeros':
        return cadena.isdigit()
    else:
        return False

def buscar_por_codigo(codigo):
    for p_mascota in Datos_mascota:
        if p_mascota[1] == codigo:
            print("**************************************")
            print("Ficha encontrada:")
            print("Nombre:", p_mascota[0])
            print("codigo:", p_mascota[1])
            print("edad:", p_mascota[2])
            print("raza:", p_mascota[3])
            print("especie:", p_mascota[4])
            print("diagnostico:", p_mascota[5])
            print("Medicamentos recetados:", p_mascota[6])
            print("**************************************")
            break
    else:
        print("codigo equivocado o eliminado")
    
def eliminar_ficha_mascota(codigo):
    for i in range(len(Datos_mascota)):
        if Datos_mascota[i][1] == codigo:
            Datos_mascota[i] = [None] * 7
            print("**********************************************")
            print(f"Ficha de mascota codigo: {codigo} eliminada.")
            print("**********************************************")
            break
    else:
        print("**********************************************")
        print("codigo incorrecto o ya eliminado")
        print("**********************************************")

def listar_mascotas_atendidos():
    print("Lista de pacientes atendidos:")
    for p_mascota in Datos_mascota:
        if p_mascota[0] is not None:
            print("**************************************")
            print("Fichas:")
            print("Nombre:", p_mascota[0])
            print("codigo:", p_mascota[1])
            print("edad:", p_mascota[2])
            print("raza:", p_mascota[3])
            print("especie:", p_mascota[4])
            print("diagnostico:", p_mascota[5])
            print("Medicamentos recetados:", p_mascota[6])
            print("**************************************")
            break

def cargar_datos_desde_json():
    global Datos_mascota
    try:
        with open('datos_pacientes.json', 'r') as file:
            Datos_mascota = np.array(json.load(file), dtype=object)
    except FileNotFoundError:
        Datos_mascota = np.empty((10, 7), dtype=object)

cargar_datos_desde_json()

def guardar_datos_en_json():
    with open('datos_mascotas.json', 'w') as file:
        json.dump(Datos_mascota.tolist(), file)
    print("***************************************")    
    print("Datos guardados en'datos_mascota.json'.")

f= 0
opc= 0


while opc !=5:
    opc = int(input("MENU\n1-crear ficha de mascota\n2-bucar codigo de mascota\n3-eliminar mascota por codigo\n4-lista de mascotas\n5-salir\nopcion: "))
    if opc == 1:
        for i in range(0, 7):
            if i == 0:
                Datos_mascota[f, i] = input("Ingrese nombre de la mascota: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'letras'):
                    Datos_mascota[f, i] = input("solo letras: ")
            elif i == 1:
                Datos_mascota[f, i] = input("Ingrese codigo: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'numeros'):
                    Datos_mascota[f, i] = input("solo numeros: ")
            elif i == 2:
                Datos_mascota[f, i] = input("ingrese edad de la mascota: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'numeros'):
                    Datos_mascota[f, i] = input("solo numeros: ")
            elif i == 3:
                Datos_mascota[f, i] = input("Ingrese raza: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'letras'):
                    Datos_mascota[f, i] = input("solo con letras: ")
            elif i == 4:
                Datos_mascota[f, i] = input("Ingrese especie: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'letras'):
                    Datos_mascota[f, i] = input("solo letras: ")
            elif i == 5:
                Datos_mascota[f, i] = input("Ingrese el diagnostico: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'letras'):
                    Datos_mascota[f, i] = input("solo letras: ")  
            elif i == 6:
                Datos_mascota[f, i] = input("Ingrese el medicamento recetado: ")
                while not only_letra_numeros(Datos_mascota[f, i], 'letras'):
                    Datos_mascota[f, i] = input("solo letras: ")     
        f += 1
    
    elif opc == 2:
        codigo_a_buscar = input("Ingrese el codigo de la mascota: ")
        buscar_por_codigo(codigo_a_buscar)
    
    elif opc ==3:
        codigo_eliminar = input("Ingrese codigo de la mascota que quiere eliminar: ")
        eliminar_ficha_mascota(codigo_eliminar)
    
    elif opc ==4:
        listar_mascotas_atendidos()

    elif opc ==5:
        guardar_datos_en_json()

        print("gracias por usar el programa")
        print("***************************************")

