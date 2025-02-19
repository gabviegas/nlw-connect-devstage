# Colocar a interface ajuda na criação de outras classes/métodos interagentes ao estabelecer um "padrão" de métodos que a classe de trabalho precisa
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import httpRequest
from src.http_types.http_response import httpResponse

class SubscribersCreator:
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo
    
    def create(self, http_request: httpRequest) -> httpResponse:
        subs_info = http_request.body["data"]
        subs_email = subs_info["email"]
        evento_id = subs_info["evento_id"]

        self.__check_sub(subs_email, evento_id)
        self.__insert_sub(subs_info)
        
        return self.__format_response(subs_info)

    def __check_sub(self, subs_email: str, evento_id: int) -> None:

        response = self.__subs_repo.select_subscriber(subs_email, evento_id)
        if response: raise Exception("SUbscriber already exists!")
    
    def __insert_sub(self, subs_info: dict) -> None:
        self.__subs_repo.insert(subs_info)
    
    def __format_response(self, subs_info: dict) -> httpResponse:
        return httpResponse(
            body={
                "data": {
                    "type": "Subscriber",
                    "count": 1,
                    "attributes": subs_info
                }
            },
            status_code = 201
        )