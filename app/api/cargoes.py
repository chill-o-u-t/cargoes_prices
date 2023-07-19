from fastapi import APIRouter, Body
from typing import List

from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.functions import Sum

from app.models import (
    CargoesP,
    CargoesP_Pydantic,
    CargoesP_Pydantic_List
)

router = APIRouter()


@router.post(
    "/",
    responses={404: {"model": HTTPNotFoundError}}
)
async def add_cargoes(cargoes=Body()):
    for date, cargoes_list in cargoes.items():
        for cargo in cargoes_list:
            obj = CargoesP(
                date=date,
                cargoes=cargo,
            )
            await obj.save()
    return await CargoesP_Pydantic_List.from_queryset(CargoesP.all())


@router.get(
    '/',
    response_model=List[CargoesP_Pydantic],
    responses={404: {"model": HTTPNotFoundError}}
)
async def get_cargoes():
    return await CargoesP_Pydantic.from_queryset(CargoesP.all())


@router.get(
    '/{cargo_date}/{declared_cost}/',
    response_model=List[CargoesP_Pydantic],
    responses={404: {"model": HTTPNotFoundError}}
)
async def add_declared_cost(cargo_date: str, declared_cost: float):
    cargoes = await CargoesP.filter(date=cargo_date).all()
    for cargo in cargoes:
        upd_value = {
            "date": cargo.date,
            "cargoes": cargo.cargoes,
            "declared_cost": declared_cost,
            "price": cargo.cargoes['rate'] * declared_cost
        }
        obj = cargo.update_from_dict(data=upd_value)
        await obj.save()
    return await CargoesP_Pydantic.from_queryset(CargoesP.filter(date=cargo_date).all())


@router.get(
    '/{cargo_date}/',
)
async def get_cargo(cargo_date: str):
    return (
        await CargoesP.annotate(sum=Sum('price'))
        .filter(date=cargo_date)
        .group_by('date')
        .values('date', 'sum')
    )

