from re import L
from fastapi import status, HTTPException
from sqlalchemy.orm.session import Session
from .. import models,schema

def get_all(db):
    get_obj = db.query(models.Item).all()
    return get_obj

def create(request:schema.BaseItem,db:Session):
    new_obj = models.Item(title=request.title,description=request.description)
    db.add(new_obj)
    db.commit()
    db.refresh(new_obj)
    return new_obj

def update(id, request:schema.BaseItem, db:Session):
    update_obj = db.query(models.Item).filter_by(id=id)
    if not update_obj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'item with id {id} is not found')
    update_obj.update(request.dict())
    db.commit()
    return "Updated succeessfully"

def remove(id,db):
    remove_obj = db.query(models.Item).filter_by(id=id)
    if not remove_obj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'item with id {id} is not found')
    remove_obj.delete()
    db.commit()
    return "Deleted succeessfully"

def show_by_id(id:int,db:Session):
    get_id_obj = db.query(models.Item).filter(models.Item.id == id).first()
    if not get_id_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'item with id {id} is not available' )
    return get_id_obj