from fastapi import APIRouter
from queries.vacations import VacationIn

router = APIRouter()

@router.post("/vacations/")
def create_vacation(vacation: VacationIn):
    print('vacation:', vacation)
    return vacation
