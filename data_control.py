import psycopg2, subprocess, hash_control, menu_control, binascii

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
        salt = hash_control.get_salt()
        key = hash_control.make_masterkey(menu_control.pw_query(), salt)
        cipherTextArr = hash_control.encrypt(password, key)
        cipherText = binascii.hexlify(cipherTextArr[0]).decode('utf-8') + ":" + (str)(cipherTextArr[1])
       # record_to_insert = (cipherText, email, username, url, app_name)
       # cursor.execute(postgres_insert_query, record_to_insert)
       # connection.commit()
        print('Cipher Text : ', cipherText)

        cipherArr = cipherText.split(':')
        cipher = str.encode(cipherArr[0])
        iv = str.encode(cipherArr[1])
        print(cipher, iv)
        plainText = hash_control.decrypt(cipher, iv, key)
        print('PlainText : ', plainText)


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