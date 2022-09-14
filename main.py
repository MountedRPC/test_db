# from connection_database import connectionDataMySQl, connectionDataPostgreSQL
#
#
# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]
#
#
# def selectMysql():
#     connection = connectionDataMySQl()
#     query = "select id, eshop, eslogin, espassword, esscr_query, esscr_request, address, unn, okpo, account, bank, phone, fax from domin_buyers"
#     cursor = connection.cursor()
#     cursor.execute(query)
#     myresult = dictfetchall(cursor)
#     return myresult
#
#
# def insertPostgreSQL():
#     connection = connectionDataPostgreSQL()
#     cursor = connection.cursor()
#     for row in selectMysql():
#         cursor.execute(
#             f'''INSERT INTO public.users_buyers(id, eshop, eslogin, espassword)
#             VALUES {row['id'], row['eshop'], row['eslogin'], row['espassword']} ''')
#     connection.commit()
#     print("Records inserted........")
#


#


import psycopg2


def connectionDataPostgreSQL():
    conn = psycopg2.connect(
        database="pyapp", user="root", password="2010"
    )
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ", data)
    return conn

def createTablePostgreSQL():
    connection = connectionDataPostgreSQL()
    cursor = connection.cursor()
    cursor.execute('''
      CREATE TABLE domin_buyers (
      id int NOT NULL  PRIMARY KEY,
      name varchar(150) DEFAULT NULL,
      login varchar(25) DEFAULT NULL,
      password varchar(25) DEFAULT NULL,
      eshop varchar(50) DEFAULT NULL,
      eslogin varchar(25) DEFAULT NULL,
      espassword varchar(25) DEFAULT NULL,
      esscr_query varchar(50) DEFAULT NULL,
      esscr_request varchar(50) DEFAULT NULL,
      address varchar(150) DEFAULT NULL,
      unn varchar(25) DEFAULT NULL,
      okpo varchar(25) DEFAULT NULL,
      account varchar(25) DEFAULT NULL,
      bank varchar(50) DEFAULT NULL,
      phone varchar(25) DEFAULT NULL,
      fax varchar(25) DEFAULT NULL,
      email varchar(50) DEFAULT NULL
    )
    ''')
    print("Table created successfully domin_buyers")
    connection.commit()


if __name__ == '__main__':
    createTablePostgreSQL()
# selectMysql()
# insertPostgreSQL()
# insertPostgreSQL()
