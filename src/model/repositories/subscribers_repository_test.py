import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip('Inserção no DB')
def test_insert():
    subs_info = {
        "name": "Gabs",
        "email": "email@email.com",
        "evento_id": 2,
        "link": "hiii"
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subs_info)

@pytest.mark.skip('Seleção no DB')
def test_select_subscriber():
    email = "email@email.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    selection = subs_repo.select_subscriber(email, evento_id)
    print(selection.nome)

@pytest.mark.skip('Ranking de links do DB')
def test_ranking():
    evento_id = 7
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)

    print()
    for item in resp:
        print(f"Link:{item.link}, Total de inscritos:{item.total}")
    