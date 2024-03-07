from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.vacations import (
    VacationIn,
    VacationRepository,
    VacationOut,
    Error,
)

router = APIRouter()

@router.post("/vacations", response_model=Union[VacationOut, Error])
def create_vacation(
    vacation: VacationIn,
    response: Response,
    repo: VacationRepository = Depends()
    ):
    return repo.create(vacation)

@router.get("/vacations", response_model=List[VacationOut])
def get_all(
    repo: VacationRepository = Depends(),
):
    return repo.get_all()

@router.put("/vacations/{vacation_ id}", response_model=Union[VacationOut, Error])
def update_vacation(
    vacation_id: int,
    vacation: VacationIn,
    response: Response,
    repo: VacationRepository = Depends()
    ) -> Union[Error, VacationOut]:
    return repo.update(vacation_id, vacation)