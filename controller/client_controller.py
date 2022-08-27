from fastapi import APIRouter, HTTPException, Request, Body
from service import client_service
from pydantic import BaseModel

router = APIRouter(prefix="/clients")


class ClientSchema(BaseModel):
    cpf: str
    rg: str
    name: str
    age: int
    height: int
    weight: float
    fidelity: bool
    active: bool


@router.get("/", tags=["clients"])
async def list_all():
    return client_service.list_all_clients()


@router.post("/", tags=["clients"])
async def create(request: Request, client: ClientSchema):
    result = client_service.create_client(client.json())
    if bool(result):
        return result
    else:
        raise HTTPException(status_code=409, detail="Duplicated entry for 'cpf'")


@router.get("/{cpf}", tags=["clients"])
async def list_all(cpf):
    return client_service.list_clients_by_cpf(cpf)
