from sqlalchemy.orm.session import Session
from .. import models,schema

def create(request:schema.BaseItem,db:Session):
    new_obj = models.Item(title=request.title,description=request.description)
    db.add(new_obj)
    db. commit()
    db.refresh(new_obj)
    return new_obj   