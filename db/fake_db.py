clients = [
        # {
        #     "cpf": "227.828.480-03",
        #     "rg": "18.361.704-6",
        #     "name": "João Marcos",
        #     "age": 27,
        #     "height": 182,
        #     "weight": 87.5,
        #     "fidelity": bool(1),
        #     "active": bool(1)
        # },
    ]


def save_client(client):
    clients.append(client)


def find_all_clients():
    return clients


def find_client_by_cpf(cpf):
    for client in clients:
        if client['cpf'] == cpf:
            return client
        else:
            return None
