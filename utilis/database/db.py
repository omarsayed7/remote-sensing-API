import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    db = None
    try:
        db = sqlite3.connect(db_file)
        test = ["amr","ehab","username","email","password"]
        cursor = db.cursor()
        sql ='''CREATE TABLE IF NOT EXISTS USERS(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20) NOT NULL,
                USERNAME CHAR(20) NOT NULL,
                EMAIL CHAR(50) NOT NULL,
                PASSWORD CHAR(20) NOT NULL
                )'''
        sql2 =''' INSERT INTO USERS(FIRST_NAME,LAST_NAME,USERNAME,EMAIL,PASSWORD)
              VALUES(?,?,?,?,?) '''
        sql3 =''' DELETE FROM USERS '''
        sql4 = ''' SELECT *,rowid FROM USERS '''
        cursor.execute(sql)
        #cursor.execute(sql2,test)
        #cursor.execute(sql2,test)
        c = cursor.execute(sql4)
        db.commit()
        for row in c:
            print (row)

    except Error as e:
        print(e)
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    create_connection(r".\users.db")