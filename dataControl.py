import psycopg2

def send(password, email, username, url, app_name):
    try:
        connection = psycopg2.connect(user='judz', password='judz', host='127.0.0.1', database='password_storage')
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


# need find password

# use to find
# """ SELECT password FROM accounts WHERE app_name """ + app_name + """
