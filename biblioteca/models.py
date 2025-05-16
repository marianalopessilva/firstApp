from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, declarative_base

# configurar banco
engine = create_engine('sqlite:///biblioteca.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    profissao = Column(String)
    salario = Column(Float)

    # representacao classe
    def __repr__(self):
        return '<Usuario: {} {}>'.format(self.nome, self.profissao, self.salario)

    # funcao para salvar no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # funcao para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_usuario(self):
        dados_usuario = {
            "id": self.id,
            "nome": self.nome,
            "profissao": self.profissao,
            "salario": self.salario,
        }
        return dados_usuario



class Livro(Base):
    __tablename__ = 'cadastro'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descricao = Column(String)
    categoria = Column(String)
    autor = Column(String)

    # representacao classe
    def __repr__(self):
        return '<Livro: {} {}>'.format(self.titulo, self.descricao, self.categoria, self.autor)

    # funcao para salvar no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # funcao para deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_livro(self):
        dados_livro = {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "autor": self.autor,
        }
        return dados_livro


# metodo para criar banco
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()

