import mysql.connector
import xml.etree.ElementTree as ET
from re import *
from hashlib import *
from db import *
from F_CRUD import *
from validaciones import *
from pymongo import MongoClient
from pymongo.errors import OperationFailure
import json
import os

#creación de las bases de datos:

try:
    # Conexión al servidor MongoDB como administrador
    admin_client = MongoClient('localhost', 27017)

    # Crear la base de datos 'Informatica1_PF'
    db = admin_client['Informatica1_PF']

    # Crear el usuario 'informatica1' con la contraseña 'info2024'
    db.command("createUser", "informatica1",
            pwd="info2024",
            roles=[{"role": "readWrite", "db": "Informatica1_PF"}])

    print("Base de datos y usuario creados exitosamente.")

    admin_client.close()

except OperationFailure:
    print('La base de datos o el usuario ya existen')


try:
    user_client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Informatica1_PF')
    db = user_client['Informatica1_PF']

    # Creación de Responsables
    resp = db['Responsables']
    #carga los datos iniciales para la conexión Responsables
    with open(os.getcwd()+"/Responsables.json") as arch:
        a = json.load(arch)
        resp.insert_many(a)
    #creación de resultados
    resul = db['Resultados']
    #carga los datos iniciales para la conexión Responsables
    with open(os.getcwd()+"/Resultados.json") as arch:
        a = json.load(arch)
        resul.insert_many(a)
    #creación de resultados
    
    print('Colecciones creadas correctaemnte')

except Exception:
    print('Ocurrió un error al crear colecciones')

#creacion base de datos mysql
# Datos de conexión
import mysql.connector
SERVIDOR = 'localhost'
USUARIO = 'root'
CONTRASENA = ''

try:
    # Conexión al servidor MySQL
    cnx = mysql.connector.connect(user=USUARIO, password=CONTRASENA, host=SERVIDOR)
    cursor = cnx.cursor()
    print("Conexión inicial exitosa")

    # Crear la base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS Informatica1_PF")
    print("Base de datos creada o ya existente")

    # Crear el usuario y otorgar privilegios
    cursor.execute("CREATE USER IF NOT EXISTS 'informatica1'@'localhost' IDENTIFIED BY 'info2024'")
    print("Usuario 'informatica1' creado o ya existente")
    cursor.execute("GRANT ALL PRIVILEGES ON Informatica1_PF.* TO 'informatica1'@'localhost'")
    print("Privilegios otorgados al usuario 'informatica1'")
    cursor.execute("FLUSH PRIVILEGES")#error
    print("Privilegios aplicados")

    # Cerrar cursor y conexión
    cursor.close()
    cnx.close()
    print("Conexión cerrada")
except Exception as e:
    print(f'No se pudo crear la base de datos{e}')

#creando tabla de responsables
import json
import os
import mysql.connector

def importJSON(path):
    with open(path, 'r') as file:
        return json.load(file)
responsables = importJSON('Final info\Responsables.json')
resultados = importJSON('Final info\Resultados.json')



# try:
conexion = mysql.connector.connect(
host='localhost',
user='informatica1',
password='info2024',
database='Informatica1_PF'
)

cursor = conexion.cursor()
resp = """
CREATE TABLE IF NOT EXISTS Responsables (
    codigo_responsable INT,
    contraseña VARCHAR(255),
    apellido VARCHAR(255),
    nombre VARCHAR(255),
    numero_documento_identidad INT,
    cargo VARCHAR(255)
)
"""
cursor.execute(resp)

for item in responsables:
    # print(item)
    query = """INSERT INTO Responsables
    (codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    val = (item['CÃ³digo responsable'], item['ContraseÃ±a'], item['Apellido'], item['Nombre'], item['Numero del documento de identidad'], item['Cargo'])
    cursor.execute(query, val)

resul = """
CREATE TABLE IF NOT EXISTS Resultados (
    Serial_probeta VARCHAR(255),
    Nombre_material VARCHAR(255),
    Resultado_ensayo_traccion FLOAT,
    Resultado_prueba_dureza INT,
    Resultado_prueba_hemocompatibilidad VARCHAR(3),
    Resultado_prueba_inflamabilidad VARCHAR(3),
    Resultado_densidad FLOAT,
    Resultado_temperatura_fusion INT,
    Fecha_realizacion DATE,
    Codigo_responsable INT
)
"""
cursor.execute(resul)

# Insertando datos en la tabla Resultados
for item in resultados:
    # print(item)
    query = """
    INSERT INTO Resultados
    (Serial_probeta, Nombre_material, Resultado_ensayo_traccion, Resultado_prueba_dureza, Resultado_prueba_hemocompatibilidad, Resultado_prueba_inflamabilidad, Resultado_densidad, Resultado_temperatura_fusion, Fecha_realizacion, Codigo_responsable)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    val = (item['Serial de la probeta'], item['Nombre del material'], item['Resultado de ensayo de tracciÃ³n'], item['Resultado prueba de dureza'], item['Resultado prueba de hemocompatibilidad'], item['Resultado prueba de inflamabilidad'], item['Resultado densidad'], item['Resultado temperatura de fusiÃ³n'], item['Fecha de realizaciÃ³n'], item['CÃ³digo responsable'])
    cursor.execute(query, val)

conexion.commit()
conexion.close()

# except Exception:
#     print('No se pudo ingresar a la base de datos.')




while True:
    op_log = val_num('''
                        \nBienvenido al Sistema de Resultados
                        \n1. Cambiar contraseña.
                        \n2. Entrar al menú principal.
                        \n3. Salir.
                        \nIngrese la opción deseada: ''')

    if op_log == 1:
        print('Escogió el cambio de clave')
        usuario = input('Ingresa el nombre de usuario: ')
        clave   = val_num('Ingrese su clave actual: ')
        clave = str(clave)
        clave_nueva = val_num('Ingrese la nueva clave: ')

        if log("Final info\\admin\\users.xml", usuario, clave):
            change_password('admin\\users.xml', usuario, clave_nueva)
        else:
            print('Usuario o clave incorrecta')

    elif op_log == 2:
        user = input('\nIngrese el usuario: ')
        clave = val_num('Ingrese la clave:')
        clave = str(clave)
        flag = log('Final info\\admin\\users.xml', user, clave)
        print(flag)

        if flag:
            while True:
                op_menu = val_num('''
                        \nMenú de Gestión de Información
                        \n1. Administradores.
                        \n2. Responsables.
                        \n3. Resultados de Pruebas.
                        \n4. Salir.
                        \nIngrese la opción deseada: ''')

                if op_menu == 1:
                    print('Menú para administradores:')
                    menuad = val_num('''1. Crear usuario administrador
                                        \n2. Ver usuario administrador
                                        \n3. Actualizar la información de un administrador. Usando la contraseña como parámetro de búsqueda
                                        \n4. Eliminar un administrador. Usando la contraseña como parámetro de búsqueda.
                                        \n5. Ingresar responsable de prueba
                                        \n6. Ver información de responsable de prueba. Usando el número de identificación como parámetro de búsqueda.
                                        \n7. Actualizar la información del responsable de la prueba. Usando el número de identificación como parámetro de búsqueda.
                                        \n8. Ver la información de todas las pruebas almacenadas asociadas a la persona responsable de la prueba
                                        \n9. Ver materiales estudiados por los diferentes responsables.
                                        \n10. Eliminar un responsable. Usando el número de identificación como parámetro de búsqueda
                                        \n11. Volver al menú principal
                                                INGRESE LA OPCION DESEADA: ''')
                    if menuad == 1:
                        nombre = input("Ingrese el nombre del nuevo administrador: ")
                        clave = input("Ingrese la clave del nuevo administrador: ")

                        # Verificar si el administrador ya existe
                        # admin_existente = consultar_admin(nombre)
                        # if admin_existente:
                        #     print("Error: El administrador ya existe.")
                        # else:
                        try:
                            agregar_admin(nombre, clave)
                        except: 
                            print(f"Administrador {nombre} no ha sido agregado correctamente.")

                    elif menuad == 2:
                        nombre_consulta = input("Ingrese el nombre del administrador a consultar: ")
                        admin = consultar_admin(nombre_consulta)

                        if admin:
                            print("Detalles del administrador:")
                            print(f"Nombre: {admin['nombre']}")
                            print(f"Clave: {admin['clave']}")
                        else:
                            print("Administrador no encontrado.")

                    elif menuad == 3:
                        nombre_actualizar = input("Ingrese el nombre del administrador a actualizar: ")
                        nueva_clave = input("Ingrese la nueva clave para el administrador: ")

                        actualizar_admin(nombre_actualizar, nueva_clave)

                    elif menuad == 4:
                        nombre_eliminar = input("Ingrese el nombre del administrador a eliminar: ")
                        eliminar_admin(nombre_eliminar)
                        
                    elif menuad == 5:
                        print("ingrese la siguiente información: ")
                        Codigo_responsable = input("codigo del responsable: ")
                        Contraseña = val_num("contraseña: ")
                        Apellido = input("apellido: ")
                        Nombre =input("nombre: ")
                        id = val_num("documento de identidad: ")
                        Cargo =input("cargo (administrador/responsable): ")
                        
                        # codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo
                        agregar_responsable_mysql(Codigo_responsable,Contraseña,Apellido, Nombre,id,Cargo )
                        print("Responsable agregado correctamente.")
                        agregar_responsable_mongo(Codigo_responsable,Contraseña,Apellido, Nombre,id,Cargo )
                        print("Responsable agregado correctamente.")

                    elif menuad == 6:
                        id_consulta = input("Ingrese el código del responsable a consultar: ")
                        responsable = consultar_responsable_mysql(id_consulta)
                        if responsable:
                            print("Detalles del responsable:")
                            print(f"Número de identificación: {responsable['id']}")
                            print(f"Nombre: {responsable['nombre']}")
                            print(f"Apellido: {responsable['apellido']}")
                        else:
                            print("Responsable no encontrado.")

                    elif menuad == 7:
                        cod_actualizar = input("Ingrese el codigo del responsable a actualizar: ")
                        nuevo_nombre = input("Ingrese el nuevo nombre del responsable: ")
                        nuevo_apellido = input("Ingrese el nuevo apellido del responsable: ")
                        nuevo_id = input("Ingrese el nuevo docuemnto de identidad del responsable: ")
                        nuevacontraseña= input("Ingrese nueva contraseña del responsable: ")
                        nuevo_cargo = input("Ingrese el nuevo cargo del responsable: ")

                        # codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo
                        actualizar_responsable_mysql(cod_actualizar, nuevacontraseña, nuevo_apellido, nuevo_nombre, nuevo_id, nuevo_cargo)
                        print("Información del responsable actualizada correctamente.")

                    elif menuad == 8:
                        pass

                    elif menuad == 9:
                        pass
                    elif menuad == 10:
                        id_eliminar = input("Ingrese el número de identificación del responsable a eliminar: ")
                        eliminar_responsable_mysql(id_eliminar)
                        print("Responsable eliminado correctamente.")

                    elif menuad == 11:
                        pass

                elif op_menu == 2:
                    while True:
                        op_user = val_num('''
                            \n1. Cambiar contraseña  
                            \n2. Ver datos personales 
                            \n3. Actualizar datos personales 
                            \n4. Ingresar nuevo resultado de prueba de material 
                            \n5. Importar resultados de prueba
                            \n6. Actualizar la información de resultados de pruebas.
                            \n7. Ver la información del resultado de una de las pruebas de material.
                            \n8. Ver todos los resultados de todas la pruebas realizadas
                            \n9. Eliminar un resultado de prueba. Usando el número de serie como parámetro de búsqueda. 
                            \n10.  Volver al menú principal ''')
                        if op_user == 1:
                            user_nom = input("ingrese el nombre del responsable: ")
                            cod_user = input("ingrese el código del responsable: ")
                            nueva_psw = input("ingrese la cotraseña nueva: ")
                            cambiar_contraseña_responsable_mysql(cod_user, user_nom,nueva_psw)
                            print("cambio de contraseña exitoso")

                        elif op_user == 2:
                            user = input("ingrese el código del responsable")
                            mostrar_responsable_mysql(user)
                        elif op_user == 3:
                            # en esta parte revisar en la funcion porque para acutalizar se compara el cosigo y no
                            # el id, entonces toca revisarlo
                            cod_actualizar = input("Ingrese el codigo del responsable a actualizar: ")
                            nuevo_nombre = input("Ingrese el nuevo nombre del responsable: ")
                            nuevo_apellido = input("Ingrese el nuevo apellido del responsable: ")
                            nuevo_id = input("Ingrese el nuevo docuemnto de identidad del responsable: ")
                            nuevacontraseña= input("Ingrese nueva contraseña del responsable: ")
                            nuevo_cargo = input("Ingrese el nuevo cargo del responsable: ")

                            # codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo
                            actualizar_responsable_mysql(cod_actualizar, nuevacontraseña, nuevo_apellido, nuevo_nombre, nuevo_id, nuevo_cargo)
                            print("Información del responsable actualizada correctamente.")
                        elif op_user == 4:
                            print("Ingrese la siguiente información: ")
                            serialP = val_num("Serial de la probeta: ")
                            nom_material = input("Nombre del material: ")
                            traccion = val_float("Resultado de ensayo de tracción [Deformación]: ")
                            dureza = val_num("Resultado prueba de dureza: ")
                            hemocompatibilidad = input("Resultado prueba de hemocompatibilidad: ")
                            inflamabilidad = input("Resultado prueba de inflamabilidad: ")
                            densidad = val_float("Resultado densidad: ")
                            fusion = val_num("Resultado temperatura de fusión: ")
                            fecha_realizacion = input("Fecha de realización: ")
                            codigo_responsable = input("Código responsable: ")
                            agregar_prueba_mysql(serialP, nom_material, traccion, dureza, hemocompatibilidad, inflamabilidad, densidad, fusion, fecha_realizacion, codigo_responsable)
                        elif op_user == 5:
                            pass
                        elif op_user == 6:
                            actu_prueba = input("ingrese el serial de la prueba a actualizar: ")
                            print("actualice la siguiente informacion: ")
                            aserialP = val_num("Serial de la probeta: ")
                            anom_material = input("Nombre del material: ")
                            atraccion = val_float("Resultado de ensayo de tracción [Deformación]: ")
                            adureza = val_num("Resultado prueba de dureza: ")
                            ahemocompatibilidad = input("Resultado prueba de hemocompatibilidad: ")
                            ainflamabilidad = input("Resultado prueba de inflamabilidad: ")
                            adensidad = val_float("Resultado densidad: ")
                            afusion = val_num("Resultado temperatura de fusión: ")
                            afecha_realizacion = input("Fecha de realización: ")
                            acodigo_responsable = input("Código responsable: ")
                            actualizar_prueba_mongo(actu_prueba, aserialP, anom_material, atraccion, adureza, ahemocompatibilidad, ainflamabilidad, adensidad, afusion, afecha_realizacion, acodigo_responsable)
                            actualizar_prueba_mysql(actu_prueba, aserialP, anom_material, atraccion, adureza, ahemocompatibilidad, ainflamabilidad, adensidad, afusion, afecha_realizacion, acodigo_responsable)
                        elif op_user == 7:
                            seralprob = input("ingrese el serial de probeta: ")
                            mostrar_prueba_mysql(seralprob)
                        elif op_user == 8:
                            seralprob = input("ingrese el serial de probeta: ")
                            mostrar_pruebas_mysql(seralprob)
                        elif op_user == 9:
                            seralprob = input("ingrese el serial de probeta: ")
                            eliminar_prueba_mysql(seralprob)
                        elif op_user == 10:
                            pass



                    
                elif op_menu == 3:
                    pass  # Código para gestionar información de resultados de pruebas

                elif op_menu == 4:
                    user_out = input('\nIngrese el usuario con el que entró al sistema: ')
                    clave_out = val_num('Ingrese la clave con la que entró al sistema:')
                    clave_out = str(clave_out)
                    if user_out == user and clave_out == clave:
                        break
                    else:
                        print('\nEl usuario o clave no fueron los mismos con los que entraste al sistema.')

                else:
                    print('\nNo has ingresado una opción válida.')

        else:
            print('\nEl usuario o clave ingresados no se encuentran en nuestra base de datos, por favor ingresa un usuario válido.')

    elif op_log == 3:
        break

    else:
        print('\nNo has ingresado una opción válida.')


