from tortoise import fields, models
from tortoise.contrib.pydantic import (
    pydantic_model_creator,
    pydantic_queryset_creator
)

from app.constants import MAX_DATE_LENGTH, MAX_TYPE_LENGTH


class CargoesP(models.Model):
    date = fields.CharField(
        max_length=MAX_DATE_LENGTH,
        null=False,
    )
    cargoes = fields.JSONField(
        null=False
    )
    declared_cost = fields.FloatField(null=True)
    price = fields.FloatField(null=True)


CargoesP_Pydantic = pydantic_model_creator(CargoesP, name='CargoesP')
CargoesP_Pydantic_List = pydantic_queryset_creator(CargoesP)
