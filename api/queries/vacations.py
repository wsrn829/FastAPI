from pydantic import BaseModel
from typing import Optional
from datetime import date
from queries.pool import pool

class Error(BaseModel):
    message: str

class VacationIn(BaseModel):
    name: str
    from_date: str
    how_long: str
    thoughts: Optional[str]

class VacationOut(VacationIn):
    id: int
    name: str
    from_date: str
    how_long: str
    thoughts: Optional[str]

class VacationRepository:
    def create(self, vacation: VacationIn) -> VacationOut:
        # connect the database
        with pool.connection() as conn:
            # get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # Run our INSERT statement
                result = db.execute(
                    """
                    INSERT INTO vacations
                        (name, from_date, how_long, thoughts)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        vacation.name,
                        vacation.from_date,
                        vacation.how_long,
                        vacation.thoughts
                    ]
                )
                id = result.fetchone()[0]
                # Return new data
                old_data = vacation.dict()
                return VacationOut(id=id, **old_data)
