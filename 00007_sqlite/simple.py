import sqlite3
from sqlite3 import Error


def main():
    print(sqlite3.sqlite_version)

    conn = create_connection("test.db")

    print("Connection", conn)

    close(conn)


def create_connection(pathToDB) -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(pathToDB)
        return conn
    except Error as e:
        print(e)


def close(conn: sqlite3.Connection):
    if conn:
        conn.close()


if __name__ == "__main__":
    main()
