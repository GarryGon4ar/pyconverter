import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType

engine = create_engine("mysql+mysqlconnector://fox:malder@localhost:3306/converter",echo=True)


Base = declarative_base()
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


class Song(Base):
    __tablename__ = 'songs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    link = sqlalchemy.Column(sqlalchemy.VARCHAR(length=512))
    email_address = sqlalchemy.Column(EmailType)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)
    def __str__(self):
        return self.link

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
                            self.name, self.fullname, self.nickname)
Base.metadata.create_all(engine)

def create_query(url, email):
    query = Song(link=url, email_address=email)
    session.add(query)
    session.commit()

    return print(f"Song(url={url}, email={email})")


