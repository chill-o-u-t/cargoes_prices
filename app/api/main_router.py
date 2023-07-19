from fastapi import APIRouter

from .cargoes import router


main_router = APIRouter()

main_router.include_router(
    router,
    prefix='/cargo',
    tags=['Cargoes']
)
