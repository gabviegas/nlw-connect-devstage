from src.http_types.http_request import httpRequest
from src.http_types.http_response import httpResponse
from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManager:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: httpRequest) -> httpResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subs = self.__subscribers_repo.select_subscribers_by_link(link, event_id)

        return self.__format_subs_by_link(subs)
    
    def get_event_ranking(self, http_request: httpRequest) -> httpResponse:
        event_id = http_request.param["event_id"]
        event_ranking = self.__subscribers_repo.get_ranking(event_id)

        return self.__format_event_ranking(event_ranking)

    def __format_subs_by_link(self, subs: list) -> httpResponse:
        formatted_subscriber = []

        for sub in subs:
            formatted_subscriber.append(
                {
                    "nome": sub.nome,
                    "email": sub.email,
                }
            )

        return httpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_subscriber),
                    "Subscribers": formatted_subscriber
                }
            },
            status_code=200
        )
    
    def __format_event_ranking(self, event_ranking: list) -> httpResponse:
        formatted_event_ranking = []

        for pos in event_ranking:
            formatted_event_ranking.append(
                {
                    "link": pos.link,
                    "total_subscribers": pos.total,
                }
            )

        return httpResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "Ranking": formatted_event_ranking
                }
            }, 
            status_code=200
        )