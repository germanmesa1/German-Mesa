from pymongo import MongoClient
import mysql.connector
import json
import os

def importJSON(path):
    with open(path, 'r') as file:
        return json.load(file)
    

#agregar reponsables mongo
def agregar_responsable_mongo(codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Responsables']
        nuevo_responsable = {
            'codigo_responsable': codigo_responsable,
            'contraseña': contraseña,
            'apellido': apellido,
            'nombre': nombre,
            'numero_documento_identidad': numero_documento_identidad,
            'cargo': cargo
        }
        collection.insert_one(nuevo_responsable)
        print(f'Responsable {nombre} agregado.')
    except Exception as e:
        print(f'Error: {e}')

#consultar responsables
def consultar_responsable_mongo(codigo_responsable):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Responsables']
        responsable = collection.find_one({'codigo_responsable': codigo_responsable})
        return responsable
    except Exception as e:
        print(f'Error: {e}')
        return None
    
def consultar_responsable_mongo(codigo_responsable, contraseña):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Responsables']
        responsable = collection.update_one({'codigo_responsable': codigo_responsable})
        return responsable
    except Exception as e:
        print(f'Error: {e}')
        return None
    
#actualizar responsables mongo
def actualizar_responsable_mongo(codigo_responsable, contraseña, apellido, nombre, numero_documento_identidad, cargo):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Responsables']
        query = {'codigo_responsable': codigo_responsable}
        nuevos_valores = {
            '$set': {
                'contraseña': contraseña,
                'apellido': apellido,
                'nombre': nombre,
                'numero_documento_identidad': numero_documento_identidad,
                'cargo': cargo
            }
        }
        collection.update_one(query, nuevos_valores)
        print(f'Responsable {nombre} actualizado.')
    except Exception as e:
        print(f'Error: {e}')

#eliminar responsables mongo
def eliminar_responsable_mongo(codigo_responsable):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Responsables']
        collection.delete_one({'codigo_responsable': codigo_responsable})
        print(f'Responsable con código {codigo_responsable} eliminado.')
    except Exception as e:
        print(f'Error: {e}')

# Pruebas mongo
def agregar_prueba_mongo(serial_probeta, nombre_material, resultado_ensayo_traccion, resultado_prueba_dureza,
                         resultado_prueba_hemocompatibilidad, resultado_prueba_inflamabilidad, resultado_densidad,
                         resultado_temperatura_fusion, fecha_realizacion, codigo_responsable):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Resultados']
        nueva_prueba = {
            'Serial_probeta': serial_probeta,
            'Nombre_material': nombre_material,
            'Resultado_ensayo_traccion': resultado_ensayo_traccion,
            'Resultado_prueba_dureza': resultado_prueba_dureza,
            'Resultado_prueba_hemocompatibilidad': resultado_prueba_hemocompatibilidad,
            'Resultado_prueba_inflamabilidad': resultado_prueba_inflamabilidad,
            'Resultado_densidad': resultado_densidad,
            'Resultado_temperatura_fusion': resultado_temperatura_fusion,
            'Fecha_realizacion': fecha_realizacion,
            'Codigo_responsable': codigo_responsable
        }
        collection.insert_one(nueva_prueba)
        print(f'Prueba {serial_probeta} agregada.')
    except Exception as e:
        print(f'Error: {e}')

#consulta prueba mongo
def consultar_prueba_mongo(serial_probeta):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Resultados']
        prueba = collection.find_one({'Serial_probeta': serial_probeta})
        return prueba
    except Exception as e:
        print(f'Error: {e}')
        return None

#actualizar prueba mongo
def actualizar_prueba_mongo(serial_probeta, nombre_material, resultado_ensayo_traccion, resultado_prueba_dureza,
                            resultado_prueba_hemocompatibilidad, resultado_prueba_inflamabilidad, resultado_densidad,
                            resultado_temperatura_fusion, fecha_realizacion, codigo_responsable):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Resultados']
        query = {'Serial_probeta': serial_probeta}
        nuevos_valores = {
            '$set': {
                'Nombre_material': nombre_material,
                'Resultado_ensayo_traccion': resultado_ensayo_traccion,
                'Resultado_prueba_dureza': resultado_prueba_dureza,
                'Resultado_prueba_hemocompatibilidad': resultado_prueba_hemocompatibilidad,
                'Resultado_prueba_inflamabilidad': resultado_prueba_inflamabilidad,
                'Resultado_densidad': resultado_densidad,
                'Resultado_temperatura_fusion': resultado_temperatura_fusion,
                'Fecha_realizacion': fecha_realizacion,
                'Codigo_responsable': codigo_responsable
            }
        }
        collection.update_one(query, nuevos_valores)
        print(f'Prueba {serial_probeta} actualizada.')
    except Exception as e:
        print(f'Error: {e}')

#eliminar prueba mongo
def eliminar_prueba_mongo(serial_probeta):
    try:
        client = MongoClient('mongodb://informatica1:info2024@localhost:27017/Inforatica1_PF')
        db = client['Inforatica1_PF']
        collection = db['Resultados']
        collection.delete_one({'Serial_probeta': serial_probeta})
        print(f'Prueba con serial {serial_probeta} eliminada.')
    except Exception as e:
        print(f'Error: {e}')



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
    
def mostrar_responsable_mysql(codigo_responsable):
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
        print(resultado)
        conexion.close()
        for registro in resultado:
            print ("{0} | {1} | {2} | {3} | {4} | {5} | " .format(registro[0], 
            registro[1], registro[2], registro[3] ,registro[4] , registro[5]))
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
def mostrar_prueba_mysql(serial_probeta):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = "SELECT * FROM Resultados WHERE Serial_probeta = %s"
        cursor.execute(query, (serial_probeta))
        resultado = cursor.fetchone()
        for registro in resultado:
            print ("{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |  " .format(registro[0], 
            registro[1], registro[2], registro[3] ,registro[4] , registro[5], registro[6], registro[7], registro[8], registro[9]))
        return resultado
    
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None
    
def mostrar_pruebas_mysql(serial_probeta):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2024',
            database='Inforatica1_PF'
        )
        cursor = conexion.cursor()
        query = "SELECT * FROM Resultados"
        cursor.execute(query, (serial_probeta))
        resultado = cursor.fetchall()
        for registro in resultado:
            print ("{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |  " .format(registro[0], 
            registro[1], registro[2], registro[3] ,registro[4] , registro[5], registro[6], registro[7], registro[8], registro[9]))
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





