import pyodbc
import os


def connectionAWS():

    db_url = os.environ['db_url']
    db_user = os.environ['db_username']
    db_pass = os.environ['db_password']
    db_name = os.environ['db_name']
    conn = pyodbc.connect('DRIVER={PostgreSQL Unicode(x64)};SERVER='+ db_url+';UID=' + db_user + ';PWD=' + db_pass + ';DATABASE=' + db_name)
    return conn
