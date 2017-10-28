import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

usuario= input('Ingrese usuario: ')
contra= input('Ingrese contrasena: ')
base= input('Ingrese Base: ')
conn = psycopg2.connect(database=base,user=usuario, password=contra, host='localhost')


print("Conexion exitosa")

cur = conn.cursor()
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

def menu_principal():
    print(' 1. Rol\n 2. Base\n 3. Tabla\n 4. Indice\n 5. Funcion\n 6. Salir')
    opcion = int(input('Digite el numero de la estructura por utilizar: '))
    if opcion == 1:
        menu_rol()
    elif opcion == 2:
        menu_base()
    elif opcion == 3:
        menu_tabla()
    elif opcion == 4:
        menu_indice()
    elif opcion == 5:
        crear_funcion()
    elif opcion == 6:
        print("\n-------------- Fin ----------------------\n")
    else:
        print('Opcion invalida')
        menu_principal()



def menu_rol():
    print(" 1.Crear Rol\n 2.Borrar Rol\n 3.Volver a menu principal")
    opcion = int(input('Digite el numero de la opcion a realizar: '))
    if opcion == 1:
        crear_roles()
    elif opcion == 2:
        borrar_roles()
    elif opcion == 3:
        menu_principal()
    else:
        print('Opcion invalida')
        menu_rol()


def crear_roles():
    nombre_rol = input('Ingrese nombre para nuevo rol: ')
    contrasena = input('Ingrese password: ')
    print('Privilegios para posible rol:\n'
          'SUPERUSER, CREATEDB, CREATEROLE, CREATEUSER, INHERIT, LOGIN, REPLICATION\n')
    privilegios = input('Ingrese privilegios: ')
    try:
        cur.execute("CREATE ROLE " + nombre_rol + " WITH PASSWORD '" + contrasena + "'" + " " + privilegios + ";")
        print("\nRol Creado\n")
    except:
         print('Intente de vuevo')

    menu_rol()


def borrar_roles():
    nombre_rol = input('Ingrese nombre del rol por borrar: ')
    try:
        cur.execute("DROP ROLE " + nombre_rol + ";")
        print("\n Rol Borrado\n")
    except:
        print('\n Rol inexistente\n')

    menu_rol()


def menu_base():
    print(" 1.Crear Base\n 2.Borrar Base\n 3.Volver a menu principal")
    opcion = int(input('Digite el numero de la opcion a realizar: '))
    if opcion == 1:
        crear_base()
    elif opcion == 2:
        borrar_base()
    elif opcion == 3:
        menu_principal()
    else:
        print('Opcion invalida')
        menu_base()


def crear_base():
    nombre_base = input('Ingrese nombre de Base Datos: ')
    try:
        cur.execute("CREATE DATABASE " + nombre_base + ";")
        print("Base Creada")
    except:
            print('\n Intente de nuevo\n')
    menu_base()



def borrar_base():
    nombre_base = input('Ingrese nombre de base por borrar: ')
    try:
        cur.execute("DROP DATABASE " + nombre_base + ";")
        print("\n Base Borrada \n")
    except:
        print('\n Intente de nuevo\n')
    menu_base()

def menu_tabla():
    print(" 1.Crear Tabla\n 2.Insertar Datos\n 3.Borrar Tabla\n 4.Actualizar Tabla\n 5.Modificar Tabla\n 6.Volver a menu principal")
    opcion = int(input('Digite el numero de la opcion a realizar: '))
    if opcion == 1:
        crear_tabla()
    elif opcion == 2:
        insertar_datos()
    elif opcion == 3:
        borrar_tabla()
    elif opcion == 4:
        actualizar_tabla()
    elif opcion == 5:
        modificar_tabla()
    elif opcion == 6:
        menu_principal()
    else:
        print('Opcion invalida')
        menu_base()

def crear_tabla():
    nombretabla = input('Nombre tabla: ')
    print('Recuerde:\n'
          'Tipo de atributos: integer, serial, decimal, double, money, varchar(n), char, bytea, timestamp, date, time, boolean')
    atributos = input('\nInserte nombre, tipo y caracteristicas de los atributos separados por ,: ')
    try:
        cur.execute("CREATE TABLE " + nombretabla + "(" + atributos + ");")
        print("Tabla Creada")
    except:
            print('\n Intente de nuevo\n')
    menu_tabla()

def insertar_datos():
    nombre = input('Nombre tabla: ')
    nom_atributos = input('Escriba el nombre de los atributos separados por , ')
    valores = input('Valores separados por , usar '' en caso de texto: ')
    try:
        cur.execute("INSERT INTO " + nombre + " (" + nom_atributos + ") VALUES (" + valores + ");")
        print("\nDatos Insertados\n")
    except:
        print('Intente de nuevo')
    menu_tabla()


def borrar_tabla():
    nombre = input('Nombre tabla que desea borrar: ')
    try:
        cur.execute("Drop table " + nombre + ";")
        print('\nTabla Borrada\n')

    except:
        print('\nIntente de nuevo\n')
    menu_tabla()


def actualizar_tabla():
    nombre = input('Nombre tabla que desea actualizar: ')
    modifica = input('Desea modificar todos los registros de una tabla si/no: ')
    registro = input('Escriba atributo/s a modificar: ')
    valor_nuevo = input('Escriba valor nuevo para registro: ')
    if modifica == 'si':
        try:
            cur.execute("Update " + nombre + " Set " + registro + "=" + valor_nuevo + ";")
            print('Tabla actualizada')
        except:
            print('Intente de nuevo')

    elif modifica == 'no':
        condicion = input('Escriba condicion: ')
        try:
            cur.execute("Update " + nombre + " Set " + registro + " = " + valor_nuevo + condicion + ";")
            print('\n Tabla Actualizada\n')
        except:
            print('Intente de nuevo')

    else:
        print("Opcion Invalida")
    menu_tabla()



def modificar_tabla():
    acciones_alter = ["0.Agregar nueva columna", "1.Borrar columna", "2.Cambiar tipo de dato de columna",
                      "3. Agregar llave primaria", "5. Borrar llave priamria"]
    print(acciones_alter)
    nombre = input('Nombre tabla que desea modificar: ')
    num_accion = int(input('Digite el numero de la accion a realizar: '))
    print(num_accion)

    if num_accion == 0:
        nombre_columna = input('Nombre columna nueva: ')
        tipo_columna = input('Tipo de dato para nueva columna: ')
        try:
            cur.execute("ALTER TABLE " + nombre + " ADD " + nombre_columna + " " + tipo_columna + ";")
            print('\nTabla Modificada\n')
        except:
            print('\nIntente de nuevo\n')
        modificar_tabla()

    elif num_accion == 1:
        nombre_columna = input('Digite el nombre de la columna a borrar: ')
        try:
            cur.execute("ALTER TABLE " + nombre + " DROP COLUMN " + nombre_columna + ";")
            print('\nTabla Modificada\n')
        except:
            print('Intente de nuevo')
        modificar_tabla()

    elif num_accion == 2:
        nombre_columna = input('Digite el nombre de la columna por cambiar: ')
        tipo_dato = input('Digite el tipo de dato: ')
        try:
            cur.execute("ALTER TABLE " + nombre + " ALTER COLUMN " + nombre_columna + " TYPE " + tipo_dato + ";")
            print('\nTabla Modificada\n')
        except:
            print('Intente de nuevo')
        modificar_tabla()

    elif num_accion == 3:
        nombre_llave = input('Nombre llave primaria: ')
        nombre_columnas = input('Ingrese las columnas separadas por , : ')
        try:
            cur.execute(
                "ALTER TABLE " + nombre + " ADD CONSTRAINT " + nombre_llave + " PRIMARY KEY (" + nombre_columnas + ");")
            print('\nTabla Modificada\n')
        except:
            print('Intente de nuevo')
        modificar_tabla()

    elif num_accion == 4:
        nombre_llave = input('Nombre llave primaria por borrar: ')
        try:
            cur.execute("ALTER TABLE " + nombre + " DROP CONSTRAINT " + nombre_llave + ";")
            print('\nTabla Modificada\n')
        except:
            print('\nIntente de nuevo\n')
        modificar_tabla()
    else:
        print('\n Opcion Invalida\n')
    menu_tabla()

def menu_indice():
    print(" 1.Crear Indice\n 2.Borrar Indice\n 3.Renombrar Indice\n 4.Reconstruir Indice\n 5.Volver a menu principal")
    opcion = int(input('Digite el numero de la opcion a realizar: '))
    if opcion == 1:
        crear_indice()
    elif opcion == 2:
        borrar_indice()
    elif opcion == 3:
        renombrar_indice()
    elif opcion == 4:
        reconstruir_indice()
    elif opcion == 5:
        menu_principal()
    else:
        print('Opcion invalida')
        menu_indice()

def crear_indice():
    nombre_index = input('Ingrese nombre indice: ')
    nombre_tabla = input('Ingrese nombre tabla: ')
    columnas = input('Ingrese columna: ')
    try:
        cur.execute("CREATE INDEX " + nombre_index + " ON " + nombre_tabla + "(" + columnas + ");")
        print('\n Indice Creado\n')
    except:
        print('\nIntente de nuevo\n')


def borrar_indice():
    nombre_index = input('Indice por borrar es: ')
    try:
        cur.execute("DROP INDEX " + nombre_index + ";")
        print("Indice Borrado")
    except:
        print('\nIntente de nuevo\n')


def renombrar_indice():
    nombre_index = input('Ingrese nombre indice: ')
    nuevo_nombre = input('Ingrese nuevo nombre de indice: ')
    try:
        cur.execute("ALTER INDEX " + nombre_index + " RENAME TO " + nuevo_nombre + ";")
        print("Indice renombrado")
    except:
        print('\nIntente de nuevo\n')


def reconstruir_indice():
    nombre_index = input('Ingrese nombre indice: ')
    try:
        cur.execute("REINDEX INDEX " + nombre_index + ";")
        print("Indice listo")
    except:
        print('\nIntente de nuevo\n')

def crear_funcion():
    valores = input('Ingrese valores/ Tipo de datos entre()')
    declarar= input('Declare las variables: ')
    como = input('As... ')
    cuerpo = input('Ingrese cuerpo de funcion incluya RETURN: ')
    cur.execute("CREATE OR REPLACE FUNCTION " +valores+
                " RETURNS "+declarar+ " AS "+como+
                " DECLARE "+declarar+
                " BEGIN "+cuerpo+
                " END; "
                "$$ LANGUAGE plpgsql;")


menu_principal()


