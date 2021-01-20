import sqlite3
from sqlite3 import Error


def create_table(conexion, create_table_sql):
    """ crea una tabla
    :param conexion: Objeto que trae la conexion
    :param create_table_sql: SQL
    :return:
    """
    try:
        c = conexion.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def guardar(datos):
    """ guardar los datos
    :param: datos a guardar
    :return
    """
    conn = sqlite3.connect('base.sqlite3')
    cursor = conn.cursor()

    sql_tabla = """ CREATE TABLE IF NOT EXISTS valores (
                                                 id integer PRIMARY KEY,
                                                 temperatura float NOT NULL,
                                                humedad float NOT NULL); """
    create_table(conn, sql_tabla)
    cursor.execute("select  count(*) from valores")

    result = cursor.fetchone()
    if result[0] == 0:
        i = 1
        for d in datos:
            parametros = i, d[0], d[1]
            sql = '''INSERT INTO valores(id,temperatura,humedad) VALUES (?,?,?)'''
            cursor.execute(sql, parametros)
            i = i + 1
        conn.commit()
        print("Datos grabados correctamente")
    else:
        print("Ya existen valores en la tabla")
