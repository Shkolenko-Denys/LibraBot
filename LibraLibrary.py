import mysql.connector
from sqlalchemy import create_engine


class LibraLibrary:
    """LibraLibrary."""

    def __init__(self):
        self.library_db = mysql.connector.connect(host="localhost",
                                                  user="root",
                                                  password="SoWhat_4")
        self.engine = create_engine(
            "mysql+pymysql://root:SoWhat_4@localhost/library")
        self.connection = self.engine.connect()

    def login(self):
        pass

    def register(self):
        pass

    def view_library_card(self):
        pass

    def order_book(self, **kwargs):
        pass
