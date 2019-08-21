
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://fox:malder'@localhost:3306/converter",echo=True)

