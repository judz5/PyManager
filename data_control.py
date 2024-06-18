import sqlite3, subprocess, hash_control, menu_control, binascii

def setup_db():
    try:
        connection = sqlite3.connect("password_storage.db")
        cursor = connection.cursor()

        make_table = '''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application TEXT NOT NULL,
            url TEXT,
            email TEXT,
            username TEXT,
            password TEXT NOT NULL
        );
        ''' 

        cursor.execute(make_table)
        connection.commit()
        print("Table Created")
    
    except sqlite3.Error as err:
        print("Error making table :: " + err)
    finally:
        connection.close()

def connect():
    try:
        connection = sqlite3.connect('password_storage.db')
        return connection
    except (Exception, sqlite3.Error) as error:
        print(error)

def send(password, email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        sqlite_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        salt = hash_control.get_salt()
        key = hash_control.make_masterkey(menu_control.pw_query(), salt)
        cipherTextArr = hash_control.encrypt(password, key)
        cipherText = binascii.hexlify(cipherTextArr[0]).decode('utf-8') + ":" + (str)(cipherTextArr[1])

        record_to_insert = (cipherText, email, username, url, app_name)
        cursor.execute(sqlite_insert_query, record_to_insert)
        connection.commit()
        print('Cipher Text : ', cipherText)

        cipherArr = cipherText.split(':')
        cipher = str.encode(cipherArr[0])
        iv = str.encode(cipherArr[1])
        print(cipher, iv)
        plainText = hash_control.decrypt(cipher, iv, key)
        print('PlainText : ', plainText)


    except (Exception, sqlite3.Error) as error:
        print(error)
    finally:
        connection.close()

def find_pass(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        sqlite_find_query = """ SELECT email, username, password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(sqlite_find_query, app_name)
        connection.commit()
        pw = cursor.fetchone()
        if not(pw==None):
            print('Email : ',pw[0])
            print('Username : ',pw[1])
            print('Password : ',pw[2])
            # subprocess.run('pbcopy', universal_newlines=True, input=pw[2])
            # print("\nPassword Copied To Clipboard.")
        else:
            print('No Account Found')
    
    except (Exception(), sqlite3.Error) as error:
        print(error)
    finally:
        connection.close()

def all_accounts():
    try:

        connection = connect()
        cursor = connection.cursor()
        sqlite_find_query = """ SELECT app_name FROM accounts """
        cursor.execute(sqlite_find_query)
        connection.commit()
        app_names = cursor.fetchall()
        return(app_names)

    except (Exception(), sqlite3.Error) as error:
        print(error)
    finally:
        connection.close()
