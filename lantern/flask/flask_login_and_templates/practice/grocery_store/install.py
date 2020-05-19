import getpass, keyring, psycopg2
import sys


def server_credential(my_server: str) -> None:
    passwd = getpass.getpass(prompt='Please input password for account: ')
    keyring.set_password(my_server, getpass.getuser(), passwd)
    print('The credential was sucessfully created for host: {} and user: {}'.format(my_server, getpass.getuser()))


def get_passwd(my_server: str):
    passwd = keyring.get_password(my_server, getpass.getuser())
    if passwd is None:
        print('Please create windows credential for host')
        sys.exit(1)
    return passwd


if __name__ == "__main__":
    server_credential('cursor_sqlalchemy_db')
    print(get_passwd('cursor_sqlalchemy_db'))
    assert get_passwd('cursor_sqlalchemy_db') == 'very_secret_password'
    server_credential('secret_key')
    print(get_passwd('secret_key'))
    assert get_passwd('secret_key') == 'aa01018c-c962-46c4-8087-c229c7e36c59'

    DATABASE = {
        "database": "cursor_sqlalchemy_db",
        "user": "cursor",
        "password": get_passwd('192.168.1.10'),
        "port": 5432,
        "host": "192.168.1.10",
    }
    con = psycopg2.connect(**DATABASE)
    with con.cursor() as cursor:
        sql = """
           SELECT * 
           FROM goods;
        """
        cursor.execute(sql)
        cursor.fetchall()
        print(cursor.fetchall())