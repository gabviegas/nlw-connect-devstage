from sqlalchemy import func, desc
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository (SubscribersRepositoryInterface):

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
    
    def select_subscribers_by_link(self, link: str, event_id: int) -> list:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.link == link,
                    Inscritos.evento_id == event_id
                )
                .all()
            )
            return data
    
    def get_ranking(self, event_id: int) -> list: # ranking de links com mais inscritos associados
        with DBConnectionHandler() as db:
            result = (
                db.session
                .query(
                    Inscritos.link,
                    func.count(Inscritos.id).label("total")
                )
                .filter(
                    Inscritos.evento_id == event_id,
                    Inscritos.link.isnot(None)
                )
                .group_by(Inscritos.link)
                .order_by(desc("total"))
                .all()
            )
        return result