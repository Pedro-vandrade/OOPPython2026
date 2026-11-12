from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/usuarios"


# Configurações do banco de dados
# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    senha=Column(String(50), nullable=False)
    e_mail=Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

def insert_Usuario(name, senha, e_mail, age):
    new_Usuario = Usuario(name=name, senha=senha, e_mail=e_mail, age=age)
    session.add(new_Usuario)
    session.commit()
    print(f'Usuário {name} adicionado com sucesso!')

def del_user(id):
    usuario = session.query(Usuario).filter_by(id=id).first()
    if usuario:
        #delete from usuario where usuario.id=id
        session.delete(usuario)
        # confirma no banco através do commit
        session.commit()
        print(f'usuário excluido conforme seu id {id}.')
    else:
        print(f'Usuário {id} não encontrado')




Base.metadata.create_all(engine) # Cria a tabela se não existir


insert_Usuario('Pedro', 123, 'pedro@gmail.com', 33)
del_user(1)
session.close()