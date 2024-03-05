from fastapi import APIRouter

router = APIRouter()

@router.post("/vacations/")
def create_vacation():
    pass