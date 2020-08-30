import mysql.connector
conn = mysql.connector.connect(host='localhost',database='DataBaseName',user='root',password='passsword')                #making connection

if conn.is_connected:
    print('Connected to DataBaseName')
conn.close()

