from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# organiza conexões com o banco de dados .db
class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///schema.db"
        self.__engine = self.__create_database_engine() # garante que ao criar um objeto dessa classe, a engine seja automaticamente criada
        self.session = None
    
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine) # cria uma sessão de trabalho no database
        self.session = session_make()
        return self # permite que a classe, ao ser chamada, garanta acesso a todos os seus atributos
    
    def __exit__(self, exc_type, exc_val, exc_tb): # exc_* são tipos de erros que podem ocorrer ao sair da classe
        self.session.close()