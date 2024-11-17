#importación de librerias

from pymongo import MongoClient
from pymongo.errors import OperationFailure
import json
import os
import mysql.connector

# Función para crear la base de datos en MongoDB
def crear_base_datos_mongo():
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

    except OperationFailure as e:
        print(f'La base de datos o el usuario ya existen: {e}')

# Función para crear colecciones y cargar datos en MongoDB
def crear_colecciones_mongo():
    try:
        user_client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Informatica1_PF')
        db = user_client['Informatica1_PF']

        # Creación de la colección Responsables
        resp = db['Responsables']
        # Carga los datos iniciales para la colección Responsables
        with open(os.path.join(os.getcwd(), "Responsables.json")) as arch:
            a = json.load(arch)
            resp.insert_many(a)

        # Creación de la colección Resultados
        resul = db['Resultados']
        # Carga los datos iniciales para la colección Resultados
        with open(os.path.join(os.getcwd(), "Resultados.json")) as arch:
            a = json.load(arch)
            resul.insert_many(a)
    
        print('Colecciones creadas correctamente')
    except Exception as e:
        print(f'Ocurrió un error al crear colecciones: {e}')

#creacion base de datos mysql
# Datos de conexión
SERVIDOR = 'localhost'
USUARIO = 'root'
CONTRASENA = ''

def crear_base_datos_my_mysql():
    try:
        cnx = mysql.connector.connect(user=USUARIO, password=CONTRASENA, host=SERVIDOR)
        cursor = cnx.cursor()
        print("Conexión inicial exitosa")

        cursor.execute("CREATE DATABASE IF NOT EXISTS Informatica1_PF")
        print("Base de datos creada o ya existente")

        cursor.execute("CREATE USER IF NOT EXISTS 'informatica1'@'localhost' IDENTIFIED BY 'info2024'")
        print("Usuario 'informatica1' creado o ya existente")
        cursor.execute("GRANT ALL PRIVILEGES ON Inforatica1_PF.* TO 'informatica1'@'localhost'")
        print("Privilegios otorgados al usuario 'informatica1'")
        cursor.execute("FLUSH PRIVILEGES")
        print("Privilegios aplicados")

        cursor.close()
        cnx.close()
        print("Conexión cerrada")

    except mysql.connector.Error as err:
        print(f"Error de conexión o ejecución de consulta: {err}")


#crear tabla de responsables mysql
def crear_tabla_responsables_mysql():
    try:
        conexion = mysql.connector.connect(
        host='localhost',
        user='informatica1',
        password='info2024',
        database='Inforatica1_PF'
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



        for item in a:
            query = """INSERT INTO Responsables
            (codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            val = (item['Código responsable'], item['Contraseña'], item['Apellido'], item['Nombre'], item['Numero del documento de identidad'], item['Cargo'])
            cursor.execute(query, val)

            conexion.commit()
            conexion.close()

    except Exception:
        print('No se pudo ingresar a la base de datos.')




#crear tabla de resultados mysql
def crear_tabla_resultados_mysql():
    try:
        conexion = mysql.connector.connect(
        host='localhost',
        user='informatica1',
        password='info2024',
        database='Inforatica1_PF'
        )


        cursor = conexion.cursor()
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
        for item in b:
            query = """
            INSERT INTO Resultados
            (Serial_probeta, Nombre_material, Resultado_ensayo_traccion, Resultado_prueba_dureza, Resultado_prueba_hemocompatibilidad, Resultado_prueba_inflamabilidad, Resultado_densidad, Resultado_temperatura_fusion, Fecha_realizacion, Codigo_responsable)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (item['Serial de la probeta'], item['Nombre del material'], item['Resultado de ensayo de tracción'], item['Resultado prueba de dureza'], item['Resultado prueba de hemocompatibilidad'], item['Resultado prueba de inflamabilidad'], item['Resultado densidad'], item['Resultado temperatura de fusión'], item['Fecha de realización'], item['Código responsable'])
            cursor.execute(query, val)

        conexion.commit()
        conexion.close()

    except Exception:
        print('No se pudo ingresar a la base de datos.')



#agregar reponsable mysql
def agregar_responsable_mysql(codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = """
        INSERT INTO Responsables (codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo))
        conexion.commit()
        conexion.close()
        print(f'Responsable {nombre} agregado.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')

#consultar responsables mysql
def consultar_responsable_mysql(codigo_responsable):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = "SELECT * FROM Responsables WHERE codigo_responsable = %s"
        cursor.execute(query, (codigo_responsable,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None
    
#actualizar responsable
def actualizar_responsable_mysql(codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = """
        UPDATE Responsables SET contraseña = %s, apellido = %s, nombre = %s, numero_documento_identidad = %s, cargo = %s
        WHERE codigo_responsable = %s
        """
        cursor.execute(query, (contraseña, apellido, nombre, numero_documento_identidad, cargo, codigo_responsable))
        conexion.commit()
        conexion.close()
        print(f'Responsable {nombre} actualizado.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')

def cambiar_contraseña_responsable_mysql(codigo_responsable,nombre, contraseña):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = """
        UPDATE Responsables SET contraseña = %s WHERE codigo_responsable = %s, nombre = %s
        """
        cursor.execute(query, (contraseña))
        conexion.commit()
        conexion.close()
        print(f'Responsable {nombre} con el código {codigo_responsable} ha cambiado su contraseña.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')

#eliminar responsablen mysql
def eliminar_responsable_mysql(codigo_responsable):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = "DELETE FROM Responsables WHERE codigo_responsable = %s"
        cursor.execute(query, (codigo_responsable,))
        conexion.commit()
        conexion.close()
        print(f'Responsable con código {codigo_responsable} eliminado.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')




# Pruebas mysql
#agregar prueba
def agregar_prueba_mysql(serial_probeta, nombre_material, resultado_ensayo_traccion, resultado_prueba_dureza,
                         resultado_prueba_hemocompatibilidad, resultado_prueba_inflamabilidad, resultado_densidad,
                         resultado_temperatura_fusion, fecha_realizacion, codigo_responsable):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = """
        INSERT INTO Resultados (Serial_probeta, Nombre_material, Resultado_ensayo_traccion, Resultado_prueba_dureza,
        Resultado_prueba_hemocompatibilidad, Resultado_prueba_inflamabilidad, Resultado_densidad, Resultado_temperatura_fusion,
        Fecha_realizacion, Codigo_responsable)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (serial_probeta, nombre_material, resultado_ensayo_traccion, resultado_prueba_dureza,
                               resultado_prueba_hemocompatibilidad, resultado_prueba_inflamabilidad, resultado_densidad,
                               resultado_temperatura_fusion, fecha_realizacion, codigo_responsable))
        conexion.commit()
        conexion.close()
        print(f'Prueba {serial_probeta} agregada.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')

#consultar prueba mysql
def consultar_prueba_mysql(serial_probeta):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = "SELECT * FROM Resultados WHERE Serial_probeta = %s"
        cursor.execute(query, (serial_probeta,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None
    
#actualizar prueba myql
def actualizar_prueba_mysql(serial_probeta, nombre_material, resultado_ensayo_traccion, resultado_prueba_dureza,
                            resultado_prueba_hemocompatibilidad, resultado_prueba_inflamabilidad, resultado_densidad,
                            resultado_temperatura_fusion, fecha_realizacion, codigo_responsable):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = """
        UPDATE Resultados SET Nombre_material = %s, Resultado_ensayo_traccion = %s, Resultado_prueba_dureza = %s,
        Resultado_prueba_hemocompatibilidad = %s, Resultado_prueba_inflamabilidad = %s, Resultado_densidad = %s,
        Resultado_temperatura_fusion = %s, Fecha_realizacion = %s, Codigo_responsable = %s
        WHERE Serial_probeta = %s
        """
        cursor.execute(query, (nombre_material, resultado_ensayo_traccion, resultado_prueba_dureza,
                               resultado_prueba_hemocompatibilidad, resultado_prueba_inflamabilidad, resultado_densidad,
                               resultado_temperatura_fusion, fecha_realizacion, codigo_responsable, serial_probeta))
        conexion.commit()
        conexion.close()
        print(f'Prueba {serial_probeta} actualizada.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')

#eliminar prueba mysql
def eliminar_prueba_mysql(serial_probeta):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = "DELETE FROM Resultados WHERE Serial_probeta = %s"
        cursor.execute(query, (serial_probeta,))
        conexion.commit()
        conexion.close()
        print(f'Prueba con serial {serial_probeta} eliminada.')
    except mysql.connector.Error as err:
        print(f'Error: {err}')



