from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'site.db')


Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()

""""
class User
    id_user int
    username str
    email str
    date_created datetime
    
"""


class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer(), primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(80), unique=True, nullable=False)
    user_date = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


class Note(Base):
    __tablename__ = 'notes'
    id_note = Column(Integer(), primary_key=True)
    notename = Column(String(40), nullable=False, unique=True)
    usernotes = Column(String(3000), unique=False, nullable=False)
    note_date = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<Note notename={self.notename} usernotes={self.usernotes}>"


# TESTES DE USER STORIES
new_user = User(id_user=1, username="luis", email="luis@gmail.com")
print(new_user)

new_note = Note(id_note=1, notename="Minha Primeira Anotação", usernotes="nova anotação aqui")
print(new_note)
