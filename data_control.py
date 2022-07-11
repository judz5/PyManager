import psycopg2, subprocess

# testing new macbook pro 14inch

def connect():
    try:
        connection = psycopg2.connect(user='judz', password='judz', host='127.0.0.1', database='password_storage')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def send(password, email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_pass(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_find_query = """ SELECT email, username, password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_find_query, app_name)
        connection.commit()
        pw = cursor.fetchone()
        if not(pw==None):
            print('Email : ',pw[0])
            print('Username : ',pw[1])
            print('Password : ',pw[2])
            subprocess.run('pbcopy', universal_newlines=True, input=pw[2])
            print("\nPassword Copied To Clipboard.")
        else:
            print('No Account Found')
    
    except (Exception(), pyscopg2.Error) as error:
        print(error)

def all_accounts():
    try:

        connection = connect()
        cursor = connection.cursor()
        postgres_find_query = """ SELECT app_name FROM accounts """
        cursor.execute(postgres_find_query)
        connection.commit()
        app_names = cursor.fetchall()
        return(app_names)

    except (Exception(), pyscopg2.Error) as error:
        print(error)
