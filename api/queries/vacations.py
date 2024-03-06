from pydantic import BaseModel
from typing import Optional
from datetime import date

class Thought(BaseModel):
    private_thought: str
    public_thought: str

class VacationIn(BaseModel):
    name: str
    from_date: str
    how_long: str
    thoughts: Optional[Thought]

class VacationRepository:
    def create(vacation: VacationIn):
        # connect the database
          # get a cursor (something to run SQL with)
            # Run our INSERT statement
              # Return new data
