import logging

from sqlalchemy.orm import Session

from app.api.endpoints.category.schemas import CategoryCreateSchema
from db.models import Category


def create_category(schema: CategoryCreateSchema, db: Session):
    entity = Category(**schema.dict())
    logging.info('Category created with id {}'.format(entity.id))
    db.add(entity)
    db.commit()
    return entity


def get_category_by_id(category_id: int, db: Session):
    entity = db.query(Category).filter(Category.id == category_id).first()
    return entity


def get_all_categories(db: Session):
    return db.query(Category).all()


def update_category(category_id: int, changed_category: CategoryCreateSchema, db: Session):
    category = get_category_by_id(category_id, db)
    if category:
        for key, value in changed_category.dict().items():
            setattr(category, key, value)
        logging.info('Category updated with id {}'.format(category.id))
        db.commit()
        db.refresh(category)
        return category
    else:
        return None


def delete_category_by_id(category_id: int, db: Session):
    category = get_category_by_id(category_id, db)
    if category:
        db.delete(category)
        db.commit()
