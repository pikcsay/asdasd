from flask import Flask
from data import db_session

from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    db_sess = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess.add(user)

    user1 = User()
    user1.surname = "Billy"
    user1.name = "Ridley"
    user1.age = 18
    user1.position = "pop"
    user1.speciality = "cook"
    user1.address = "module_3"
    user1.email = "chef@mars.org"
    user1.hashed_password = "cop"
    db_sess.add(user1)

    user2 = User()
    user2.surname = "Andrey"
    user2.name = "Bob"
    user2.age = 50
    user2.position = "developer"
    user2.speciality = "programming"
    user2.address = "module_99"
    user2.email = "dev_yandex@mars.org"
    user2.hashed_password = "cip"
    db_sess.add(user2)

    user3 = User()
    user3.surname = "Vany"
    user3.name = "Sidney"
    user3.age = 34
    user3.position = "cop"
    user3.speciality = "bull"
    user3.address = "module_1"
    user3.email = "fifty@mars.org"
    user3.hashed_password = "pac"
    db_sess.add(user3)

    db_sess.commit()

    app.run(host='localhost', port=5000)


if __name__ == '__main__':
    main()
