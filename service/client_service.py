from db import fake_db
import json


def list_all_clients():
    return fake_db.find_all_clients()


def create_client(json_client):
    client = json.loads(json_client)
    if fake_db.find_client_by_cpf(client['cpf']) is None:
        fake_db.save_client(client)
        return "Client successfully registered"
    else:
        return 0


def list_clients_by_cpf(cpf):
    return fake_db.find_client_by_cpf(cpf)
