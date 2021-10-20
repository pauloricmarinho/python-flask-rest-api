from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db_produtos.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Fabricante(Base):
    __tablename__='tbl_fabricantes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)
    

    def __repr__(self):
        return '<Fabricante {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Produto(Base):
    __tablename__='tbl_podutos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    valor = Column(Float)
    fabricante_id = Column(Integer, ForeignKey('tbl_fabricantes.id'))
    fabricante = relationship("Fabricante")

    def __repr__(self):
        return '<Produto {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuario(Base):
    __tablename__='tbl_usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()