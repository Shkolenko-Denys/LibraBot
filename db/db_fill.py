# -*- coding: utf-8 -*-

from app import app, db
from db.models import User, Book, Log, Role, Author, Publisher, Genre, Udc

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root',
             nickname='root@gmail.com',
             password='password',
             major='administrator',
             headline=u"Temporary Administrator One",
             about_me=u"Graduated from the Department of Management, and "
                      u"likes to read, so I work as a librarian part-time.")
user1 = User(name=u'akarin',
             nickname='akarin@Gmail.com',
             password='123456',
             major='Computer Science',
             headline=u"ordinary student")
user2 = User(name=u'test',
             nickname='test@test.com',
             password='123456')
user3 = User(name=u'Xiao Ming',
             nickname='xiaoming@163.com',
             password='123456')
user4 = User(name=u'Li Hua',
             nickname='lihua@yahoo.com',
             password='123456')

author1 = Author(surnames_initials="Shevchenko A.A.")
author2 = Author(surnames_initials="Іваненко В.В.")
author3 = Author(surnames_initials="Петренко П.П.")

publisher1 = Publisher(publisher="New York")
publisher2 = Publisher(publisher="HeyWorld")
publisher3 = Publisher(publisher="AboutWld")

genre1 = Genre(genre="Драма")
genre2 = Genre(genre="Історія")
genre3 = Genre(genre="Комедія")

udc1 = Udc(udc_number=123)
udc2 = Udc(udc_number=124)
udc3 = Udc(udc_number=125)

book1 = Book(author1, publisher1, genre1, udc1,
             title=u"Передчуття",
             isbn='9787115373991',
             pub_year=2004,
             tags_string=u"history, world, people",
             image='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1637012564',
             summary=u"""Повільне життя провінційного приморського містечка N раптом порушує локальний скандал, який розгортається навколо чоловіка, що пішов з життя. Про місце його поховання знають лише дружина та друг, але вони категорично відмовляються повідомити про це іншим. Таким нібито був заповіт небіжчика, дивака, закоханого у море.""")
book2 = Book(author1, publisher1, genre1, udc1,
             title=u"Червона таблетка",
             isbn='9787560926995',
             pub_year=2004,
             tags_string=u"history, world, school",
             image='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1637012564',
             summary=u"""У книзі зібрані найважливіші наукові відкриття в галузі нейрофізіології, які допоможуть читачеві розібратися в принципах роботи мозку й ефективніше використовувати його для вирішення важливих завдань. Ви навчитеся розуміти поведінку й мотиви інших людей і взаємодіяти з ними для досягнення цілей.""")
book3 = Book(author1, publisher1, genre1, udc1,
             title=u"Місто дівчат",
             isbn="9787111251217",
             pub_year=2008,
             tags_string=u"history, world",
             image='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1637012564',
             summary=u"""Це інтригуючий роман про жіночу сексуальність і свободу, про відвагу бути собою і право жити так, як тобі хочеться. А ще — історія дуже незвичайного кохання, на яке наклала свою тінь війна, та справжньої дружби, яку нелегко знайти, зрозуміти та оцінити, особливо в такому непростому і мінливому місті, як Нью-Йорк.""")
book4 = Book(author1, publisher1, genre1, udc1,
             title=u"Memory",
             isbn="9787111321330",
             pub_year=2007,
             tags_string=u"world, school",
             image='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1637012564',
             summary=u"""Метод ненасильницького спілкування (ННС) реально покращує життя тисяч людей. Він застосовується і в подружній спальні, і в класній кімнаті, і за круглим столом, і на лінії фронту. Корпорації, організації та уряди, що приймають метод ННС, швидко досягають значного прогресу у вирішенні своїх внутрішніх і зовнішніх проблем.""")
book5 = Book(author1, publisher1, genre1, udc1,
             title=u"About Memory",
             isbn="9787517010845",
             pub_year=2006,
             tags_string=u"programming, school",
             image='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1637012564',
             summary=u"""This book provides a comprehensive introduction to computer algorithms. The analysis of each algorithm is easy to understand and very interesting, and maintains mathematical rigor.""")
book6 = Book(author1, publisher1, genre1, udc1,
             title=u"Big Money",
             isbn="9787111187776",
             pub_year=2005,
             tags_string=u"world, programming",
             image='https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1637012564',
             summary=u"Хто не хоче, шукає причини. Хто хоче, шукає можливості. Ця книга про людей, які завжди шукають можливості і знаходять їх. Все хороше в цьому Світі придумано людьми, які хотіли заробити. Підприємцями і бізнесменами. Ця книга про них. Про тих, хто кожен день робить цей світ кращим, розвиваючи свій бізнес, створюючи робочі місця і сплачуючи податки.")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, author1, author2, author3,
                    publisher1, publisher2, publisher3, genre1, genre2, genre3,
                    udc1, udc2, udc3,
                    book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
