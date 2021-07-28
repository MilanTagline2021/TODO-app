from pydantic import BaseModel

class BaseItem(BaseModel):
    title : str
    description : str

    class Config():
        orm_mode = True