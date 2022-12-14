import sys
import os
import json
import pymysql

def getConnection():
    # connection arguments to connect to AWS RDS.
    connection = pymysql.connect(host='group7cc.cvbohwaai2ht.eu-west-2.rds.amazonaws.com',
                                 port=3306,
                                 user='group7',
                                 password='ccgroup7',
                                 database='group7')
    return connection

def insert_currency(id, symbol):
    connection = getConnection()
    cursor = connection.cursor()
    query = "INSERT INTO coins (id, symbol) VALUES (%s, %s)"
    cursor.execute(query, (id, symbol))
    connection.commit()
    connection.close()
    

def select_currency(symbol):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT id FROM coins WHERE symbol like (%s)"
    cursor.execute(query, (symbol))
    full_name = cursor.fetchone()
    print(''.join(full_name))
    connection.close()
    if not full_name:
        return 'No record found', ''
    else:
        return ''.join(full_name)

if __name__ == '__main__':
    insert_currency(id='british-pound-sterling', symbol = "GBP")
    id, symbol = select_currency('GBP')
    print(id, symbol)


def delete_currency(symbol):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT id FROM coins WHERE symbol =%s"
    cursor.execute(query, (symbol))
    records = cursor.fetchone()
    if records:
        query = "DELETE FROM coins where symbol like %s"  
        cursor.execute(query, (symbol))
        connection.commit()
        connection.close()
        return True
    else:
        connection.close()
        return False


def update_currency(id, symbol):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT id FROM coins WHERE symbol=%s"
    cursor.execute(query, (symbol))
    records = cursor.fetchone()
    if records:
        query = "UPDATE coins SET id = %s WHERE symbol = %s"    
        cursor.execute(query, (id, symbol))
        connection.commit()
        connection.close()
        return f'Modified name for {symbol}'
    else:
        query = "INSERT INTO coins (id, symbol) VALUES (%s, %s)"    
        cursor.execute(query, (id, symbol))
        connection.commit()
        connection.close()
        return f'Created new record for {symbol}'


def insert_user(name, password, role):
    
    connection = getConnection()
    cursor = connection.cursor()
    query = "INSERT INTO users (userID, pw, userRole) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, password, role))
    connection.commit()
    connection.close()
    
       
def select_user(name):

    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT userID, pw, userRole FROM users WHERE userID like %s"
    cursor.execute(query, (name))
    account = cursor.fetchone()
    connection.close()
    return account
