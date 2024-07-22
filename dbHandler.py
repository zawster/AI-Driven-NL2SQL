from openaiHandler import *
from config import *
import mysql.connector

chunk_size = 10000
def get_db_connection():
    try:
        print("SQL db connection is getting created...")
        connection = mysql.connector.connect(host=DB_HOST,
                                            database=DATABASE_NAME,
                                            user= DB_USER,
                                            password=DB_PASSWORD,
                                            port=DB_PORT)
        print("#### DB Connection got created...")
        return connection
    except Exception as exp:
        print(f"There is some issue in creating SQL connection. Issue: {exp}")
        raise

def get_list_of_tables(cursor):
    """
    This function gets the list of tables available
    in the database connected to the mysql server
    and returns the same
    :param cursor:
    :return: list of tables
    """
    try:
        query = "show tables;"
        cursor.execute(query)
        tables = cursor.fetchall()
        table_list = []
        for each_table in tables:
            table_list.append(each_table[0])
        print(f"Number of tables fetched: {len(table_list)}")
        return table_list
    except Exception as exp:
        print(f"There is some issue in get the tables list. Issue: {exp}")
        raise


def get_tables_db_schema(cursor, tables):
    try:
        db_schema = {}

        for table in tables:
            query = f"SHOW FULL COLUMNS FROM {DATABASE_NAME}.{table};"
            cursor.execute(query)
            columns = cursor.fetchall()

            column_details = {}
            for column in columns:
                column_name = column[0]
                column_description = column[-1]
                column_details[column_name] = column_description

            db_schema[table] = column_details
        return db_schema
    except Exception as exp:
        print(f"There is some issue in extracting table schema. Issue: {exp}")
        raise

def get_table_schema():
    try:
        connection = get_db_connection()
        db_schema = {}
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            list_of_tables = get_list_of_tables(cursor)
            db_schema = get_tables_db_schema(cursor, list_of_tables)

        cursor.close()
        connection.close()


        return db_schema, list_of_tables
    except Exception as exp:
        print(f"There is some issue in getting the information from database. Issue: {exp}")
        raise