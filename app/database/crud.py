from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.models import Item as ItemModel
from app.schemas import ItemCreate, ItemUpdate

def get_items(db: Session) -> List[ItemModel]:
    """Obtener todos los items"""
    return db.query(ItemModel).all()

def get_item_by_id(db: Session, item_id: int) -> Optional[ItemModel]:
    """Obtener un item por ID"""
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()

def create_item(db: Session, item: ItemCreate) -> ItemModel:
    """Crear un nuevo item"""
    db_item = ItemModel(name=item.name, price=item.price, is_active=item.is_active)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: ItemUpdate) -> Optional[ItemModel]:
    """Actualizar un item por ID"""
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.price = item.price
        db.commit()
        db.refresh(db_item)
        return db_item
    return None

def delete_item(db: Session, item_id: int) -> bool:
    """Eliminar un item por ID"""
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
