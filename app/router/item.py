from app.models import Item
from fastapi import Depends, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from .. import schema, database
from ..backend import item

router = APIRouter(
    prefix='/TODO',
    tags=['TODO']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schema.BaseItem, db:Session = Depends(database.get_db)):
    return item.create(request,db)