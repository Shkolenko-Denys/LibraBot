import mysql.connector
from sqlalchemy import create_engine
from config import *


class LibraLibrary:

    def __init__(self):
        self.library_db = mysql.connector.connect(
            host=library_db_host,
            user=library_db_user,
            password=library_db_password
        )
        self.engine = create_engine(
            f"{library_db_dialect}+{library_db_driver}://{library_db_user}:"
            f"{library_db_password}@{library_db_host}/{library_db_name}")
        self.connection = self.engine.connect()

    def find_phone_number(self, phone_number):
        return True

    def login(self, phone_number, password):
        return True

    def register(self, surname, name, patronymic, birthday, phone_number,
                 email, telegram_username, address, passport_number):
        return True

    def view_library_card(self):
        pass

    def order_book(self):
        pass


libra_library = LibraLibrary()
