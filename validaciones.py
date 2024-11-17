import xml.etree.ElementTree as ET
import hashlib
import re
import os

def val_num(num):
    while True:
        try:
            entrada = int(input(num))
            return entrada
        except ValueError:
            print("Por favor ingrese solo números")

def val_float(num):
    while True:
        try:
            entrada = float(input(num))
            return entrada
        except ValueError:
            print("Ingrese números flotantes")

def val_alfabetico(input_str):
    while True:
        try:
            entrada = bool(re.match("^[a-zA-Z]+$", input_str))
            return entrada
        except:
            print("Ingrese caracteres alfabéticos")

def val_num2(input_str):
    while True:
        try:
            entrada = bool(re.match("^[0-9]+$", input_str))
            return entrada
        except:
            print("Ingrese solo números")

def val_float2(input_str):
    while True:
        try:
            entrada = bool(re.match("^[0-9]+\\.[0-9]+$", input_str))
            return entrada
        except:
            print("Ingrese números flotantes válidos")

def is_valid_yes_no(input_str):
    while True:
        try:
            entrada = input_str.lower() in ['si', 'no']
            return entrada
        except:
            print("Ingrese la opción correcta")

def log(texto, usuario, clave):
    try:
        if not os.path.exists(texto):
            print(f"Error: Archivo '{texto}' no encontrado.")
            return False

        archivo = ET.parse(texto)
        root = archivo.getroot()  # Raíz del XML
        flag = False  # Bandera por si se encuentran usuarios

        for rama in root:
            u_xml = rama.find('nombre')  # Usuario extraído del XML
            c_xml = rama.find('clave')  # Contraseña extraída del XML
            if usuario == u_xml.text and clave == c_xml.text:
                flag = True  # Bandera verdadera cuando se encuentra el usuario
                break

        return flag
    except Exception as e:
        print(f"Error: {e}")
        return False

def change_password(username, old_password, new_password):
    try:
        tree = ET.parse('admin/users.xml')
        root = tree.getroot()
        hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        for user in root.findall('usuario'):
            user_name = user.find('nombre').text
            user_pass = user.find('clave').text
            if user_name == username and user_pass == hashed_old_password:
                user.find('clave').text = hashed_new_password
                tree.write('admin/users.xml')
                break
    except Exception as e:
        print(f"Error al cambiar contraseña: {e}")

XML_PATH = 'Final info\\admin\\users.xml'

def agregar_admin(nombre, clave):
    try:
        tree = ET.parse(XML_PATH)
        root = tree.getroot()

        nuevo_admin = ET.Element('admin')
        nombre_elem = ET.SubElement(nuevo_admin, 'nombre')
        nombre_elem.text = nombre
        clave_elem = ET.SubElement(nuevo_admin, 'clave')
        clave_elem.text = clave

        root.append(nuevo_admin)
        tree.write(XML_PATH)
        print(f'Administrador {nombre} agregado.')
    except Exception as e:
        print(f"Error al agregar administrador: {e}")

def consultar_admin(nombre):
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    for admin in root.findall('admin'):
        if admin.find('nombre').text == nombre:
            return {
                'nombre': admin.find('nombre').text,
                'clave': admin.find('clave').text
            }
    return None

def actualizar_admin(nombre, nueva_clave):
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    for admin in root.findall('admin'):
        if admin.find('nombre').text == nombre:
            admin.find('clave').text = nueva_clave
            tree.write(XML_PATH)
            print(f'Administrador {nombre} actualizado.')
            return
    print(f'Administrador {nombre} no encontrado.')

def eliminar_admin(nombre):
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    for admin in root.findall('admin'):
        if admin.find('nombre').text == nombre:
            root.remove(admin)
            tree.write(XML_PATH)
            print(f'Administrador {nombre} eliminado.')
            return
    print(f'Administrador {nombre} no encontrado.')


            
                              