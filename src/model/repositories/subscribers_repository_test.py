import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip('Inserção no DB')
def test_insert():
    subs_info = {
        "name": "meu nome",
        "email": "email@email.com",
        "evento_id": 2,
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