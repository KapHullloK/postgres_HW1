import psycopg2
import csv

connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)


def insert_data_from_csv(filename, tablename, conn):
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        with conn.cursor() as cursor:
            for row in reader:
                placeholders = ','.join(['%s'] * len(row))
                query = f"INSERT INTO {tablename} VALUES ({placeholders})"
                cursor.execute(query, row)
    conn.commit()


insert_data_from_csv('north_data/employees_data.csv', 'employee', connection)

insert_data_from_csv('north_data/customers_data.csv', 'customers', connection)

insert_data_from_csv('north_data/orders_data.csv', 'orders', connection)

connection.close()
