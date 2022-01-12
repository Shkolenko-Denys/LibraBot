from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash

import config
from app import db
from db.models import Book, Log


class LibraLibrary:
    """Class for working with the 'Libra' library database."""

    def __init__(self, database=config.SQLALCHEMY_DATABASE_URI):
        self.engine = create_engine(database)
        self.connection = self.engine.connect()

    def get_user_name(self, user_id):
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")
        sql_content_query = text(f"""SELECT name FROM users
                                     WHERE id = {user_id}""")
        content = self.connection.execute(sql_content_query).fetchone()
        if content:
            return content[0]
        else:
            return None

    def find_nickname(self, nickname):
        if not isinstance(nickname, str):
            raise TypeError("nickname must be a string")
        sql_content_query = text("""SELECT nickname FROM users""")
        content = self.connection.execute(sql_content_query).fetchall()
        return nickname in list(item[0] for item in content)

    def register(self, id, nickname, name, password, about_me):
        if not isinstance(nickname, str):
            raise TypeError("nickname must be a string")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(password, str):
            raise TypeError("password must be a string")
        if not isinstance(about_me, str):
            raise TypeError("about_me must be a string")
        if self.find_nickname(nickname):
            raise ValueError("the nickname already exists")
        sql_content_query = text(
            f"""INSERT INTO users
            (id, nickname, name, password_hash, about_me,
            role_id, about_me_html, member_since)
            VALUES
            ({id}, '{nickname}', '{name}',
            '{generate_password_hash(password)}', '{about_me}', 1,
            '<p>{about_me}</p>', '{str(datetime.now())}')""")
        self.connection.execute(sql_content_query)

    def get_top5_books(self):
        sql_content_query = text(
            """SELECT books.id, books.title, books.pub_year,
            authors.surnames_initials, genres.genre
            FROM books
            JOIN authors ON authors.id = books.author_id
            JOIN genres ON genres.id = books.genre_id
            ORDER BY books.numbers
            LIMIT 5""")
        return self.connection.execute(sql_content_query).fetchall()

    def get_book(self, id):
        sql_content_query = text(f"""SELECT * FROM books WHERE id = {id}""")
        return self.connection.execute(sql_content_query).fetchone()

    def order_book(self, user_id, book_id):
        sql_content_query = text(
            f"""INSERT INTO logs
            (user_id, book_id, borrow_timestamp, return_timestamp, returned)
            VALUES
            ({user_id}, {book_id}, '{str(datetime.now())}',
            '{str(datetime.now() + timedelta(days=60))}', 0)""")
        self.connection.execute(sql_content_query)

    def comment(self, user_id, book_id, comment):
        sql_content_query = text(
            f"""INSERT INTO comments
                    (user_id, book_id, comment, create_timestamp,
                    edit_timestamp, deleted)
                    VALUES
                    ({user_id}, {book_id}, '{comment}', '{str(datetime.now())}',
                    '{str(datetime.now())}', 0)""")
        self.connection.execute(sql_content_query)

    def get_genres(self):
        sql_content_query = text("""SELECT genre FROM genres""")
        content = self.connection.execute(sql_content_query).fetchall()
        return list(item[0] for item in content)

    def get_by_genre(self, genre):
        if not isinstance(genre, str):
            raise TypeError("genre must be a string")
        sql_content_query = text(
            f"""SELECT books.id, books.title, books.pub_year, authors.surnames_initials
            FROM books
            JOIN authors ON authors.id = books.author_id
            WHERE books.id = (SELECT id FROM genres WHERE genre = '{genre}')""")
        return self.connection.execute(sql_content_query).fetchall()

    def count_books(self):
        sql_content_query = text("""SELECT COUNT(*) FROM books""")
        return self.connection.execute(sql_content_query).fetchone()[0]


libra_library = LibraLibrary()
