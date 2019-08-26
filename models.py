import datetime
from sqlalchemy import create_engine
from sqlalchemy import orm, Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType

engine = create_engine("mysql+mysqlconnector://fox:malder@localhost:3306/converter",echo=True)


Base = declarative_base()
Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    link = Column(VARCHAR(length=512))
    email_address = Column(EmailType)
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
                            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

def create_query(url, email):
    query = Song(link=url, email_address=email)
    session.add(query)
    session.commit()

    return print(f"Song(url={url}, email={email})")


