import sqlite3

conn = sqlite3.connect("login_credentials")
c = conn.cursor()


# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS login_creds(username TEXT, password TEXT)')


# def data_entry():
#     c.execute('INSERT INTO login_creds values("eddie", "123456")')
#     conn.commit()


# def delete_db():
#     c.execute('DELETE FROM login_creds WHERE name = "eddie"')
#     conn.commit()


def read_from_db():
    c.execute('SELECT * FROM login_creds')

    data = c.fetchall()
    print(data)
    print(("123", "123") in data)
    # for row in c.fetchall():
    #     print(row)

# def read_db():
#     data = c.fetchall()
#     print(data)
#     print(("123", "123") in data)

# create_table()
# data_entry()
# delete_db()
read_from_db()

c.close()
conn.close()
