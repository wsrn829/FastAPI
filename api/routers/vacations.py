from fastapi import APIRouter, Depends
from typing import Union
from queries.vacations import (
    VacationIn,
    VacationRepository,
    VacationOut,
    Error,
)

router = APIRouter()

@router.post("/vacations", response_model=Union [VacationOut, Error])
def create_vacation(
    vacation: VacationIn,
    repo: VacationRepository = Depends()
    ):
    return repo.create(vacation)
