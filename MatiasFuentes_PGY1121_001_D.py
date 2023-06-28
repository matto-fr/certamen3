import os
os.system("cls")

Menu = '''
1. Grabar enomiendas
2. Buscar enomiendas
3. Listar encomiendas
4. Salir
'''
lista_numero_enc = []
lista_tipo_enc = []
lista_nombres_dest = []
lista_rut_dest = []
lista_peso_kg = []
lista_precios = []
lista_ciudades_dest = []

cont_sobre = 0
cont_paquete = 0

print(Menu)

def grabar_enc():
    while True:
        try:
            while True:
                for i in lista_numero_enc:                        
                        lista_numero_enc.append(i)
                try:
                    tipo_encomienda = int(input('''Seleccione el tipo de encomienda:
                    1. Sobre
                    2. Paquete               
                    '''))
                    cont_sobre = 0
                    cont_paquete = 0
                    if tipo_encomienda == 1:
                        lista_tipo_enc.append('SOBRE')
                        cont_sobre += 1
                    elif tipo_encomienda == 2:
                        lista_tipo_enc.append('PAQUETE')
                        cont_paquete += 1
                    else:
                        print("Error, la oción seleccionada debe ser 1 o 2")
                except:
                    print("Ha ocurrido una excepción")
                try:
                    nombre_dest = input("Ingrese el nombre del destinatario: ").upper()
                    if len(nombre_dest) >= 2 and len(nombre_dest) <= 30:
                        lista_nombres_dest.append(nombre_dest)
                    else:
                        print("Error, el nombre debe contener entre 2 y 30 caracteres")
                except:
                    print("Ha ocurrido una excepción")
                try:
                    rut_dest = input("Ingrese el rut del destinatario: ").upper()
                    if len(rut_dest) > 0:
                        lista_rut_dest.append(rut_dest)
                    else:
                        print("Error, el rut debe tener como penúltimo caracter un guión")
                except:
                    print("Ha ocurrido una excepción")
                try:
                    peso_kg = float(input("Ingrese el peso de la encomienda: "))
                    if peso_kg >= 0.1:
                        lista_peso_kg.append(peso_kg)
                    else:
                        print("Error, el peso mínimo debe ser 0.1 kg")
                except:
                    print("Ha ocurrido una excepción")
                try:
                    precio = int(input("Ingrese el precio de la encomienda: "))
                    if precio >= 2000:
                        lista_precios.append(precio)
                    else:
                        print("Error, el precio mínimo debe ser $2000")
                except:
                    print("Ha ocurrido una excepción")
                try:
                    ciudad_dest = (input("Ingrese la ciudad de destino de la encomienda: ")).upper()
                    if len(ciudad_dest) >= 3:
                        lista_ciudades_dest.append(ciudad_dest)
                    else:
                        print("Error, la ciudad debe tener al menos 3 caracteres")
                except:
                    print("Ha ocurrido una excepción")
                try:
                    continuar = int(input('''¿Desea agregar otra encomienda?:
                               1. Si
                               2. No\n'''))
                    if continuar == 1:
                        continue
                    elif continuar == 2:
                        break
                    else:
                        print("Error, la opción selecionada debe ser 1 o 2")
                except:
                    print("Ha ocurrido una excepción")
        except:
            print("Ha ocurrido una excepción")
        break

    # fin while

def buscar_enc():
    while True:
        try:
            rut_dest = input("Ingrese rut para buscar encomienda: ")
            print(f'LISTADO DE ENCOMIENDAS DE [{rut_dest}]')
            print("N° |  TIPO    |     NOMBRE DESTINATARIO      |   RUT DESTINATARIO  | PESO EN KG |  PRECIO   |  CIUDAD DE DESTINO  |")
            print("---|----------|------------------------------|---------------------|------------|-----------|---------------------|")
            for i in range(len(lista_numero_enc)):
                if rut_dest == lista_rut_dest[i]():
                    print(f"{i+1}|{lista_tipo_enc[i]}|{lista_nombres_dest[i]}|{lista_rut_dest[i]}|{lista_peso_kg[i]}|{lista_precios[i]}|{lista_ciudades_dest[i]}|")

        except:
            print("Ha ocurrido una excepción")
        break
    # fin while

def listar_enc():
    while True:
        try:
            print("LISTADO ENCOMIENDAS")
            print("-------------------------------")
            print("N° |  TIPO    |     NOMBRE DESTINATARIO      |   RUT DESTINATARIO  | PESO EN KG |  PRECIO   |  CIUDAD DE DESTINO  |")
            print("---|----------|------------------------------|---------------------|------------|-----------|---------------------|")
            for i in range(len(lista_numero_enc)):
                  print(f"{i+1}|{lista_tipo_enc[i]}|{lista_nombres_dest[i]}|{lista_rut_dest[i]}|{lista_peso_kg[i]}|{lista_precios[i]}|{lista_ciudades_dest[i]}|")
            print(f"TOTAL SOBRES:   {cont_sobre}")
            print(f"TOTAL PAQUETES: {cont_paquete}")
        except:
            print("Ha ocurrido una excepción")
        break
    # fin while

while True:
        try:
            print(Menu)
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                grabar_enc()
            elif opc == 2:
                buscar_enc()
            elif opc == 3:
                listar_enc()
            elif opc == 4:
                print('''
Matías Fuentes Riffo
Versión del software: [1.0]
                      ''')
                break
            else:
                print("Error, la opción seleccionada debe ser 1, 2, 3 o 4")
        except:
            print("Ha ocurrido una excepción")
# fin while