from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer

# classe pareada com a tabela SQL
class Eventos(Base):
    __tablename__ = "Eventos" # nome da tabela no arquivo SQL

    # colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True) 
    nome = Column(String, nullable=False)