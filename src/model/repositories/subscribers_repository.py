from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class SubscribersRepository:

    # cria uma função de inserção de novos eventos no db
    def insert(self, subs_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome=subs_info.get("name"),
                    email=subs_info.get("email"),
                    link=subs_info.get("link"),
                    evento_id=subs_info.get("evento_id")
                )
                db.session.add(new_subscriber)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.email == email, 
                    Inscritos.evento_id == evento_id
                )
                .one_or_none()
            )
            return data