from app.models import Item
from typing import List
from fastapi import Depends, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from .. import schema, database
from ..backend import item

router = APIRouter(
    prefix='/TODO',
    tags=['TODO']
)

@router.get('/', response_model=List[schema.BaseItem], status_code=status.HTTP_200_OK)
def get_all(db:Session = Depends(database.get_db)):
    return item.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schema.BaseItem, db:Session = Depends(database.get_db)):
    return item.create(request,db)

@router.put('/',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schema.BaseItem, db:Session = Depends(database.get_db)):
    return item.update(id, request, db)

@router.delete('/',status_code=status.HTTP_204_NO_CONTENT)
def remove(id:int, db:Session = Depends(database.get_db)):
    return item.remove(id, db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schema.BaseItem)
def get_by_id(id:int, db:Session = Depends(database.get_db)):
    return item.show_by_id(id, db)

