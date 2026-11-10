import sqlite3


DATABASE_NAME = "reading_list.db"


def create_table():
    with sqlite3.connect(DATABASE_NAME) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )"""
        )


def add_book(title, author):
    pass


def list_books():
    pass


def update_book(book_id, title, author):
    pass


def delete_book(book_id):
    pass


def main():
    create_table()
    print("Build a menu to manage your reading list.")


if __name__ == "__main__":
    main()