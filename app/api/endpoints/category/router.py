from typing import List

from fastapi import APIRouter, Depends, Request, Response, status, HTTPException
from sqlalchemy.orm import Session

import app.api.endpoints.category.CRUD as category_crud
from app.api.endpoints.category.schemas import CategorySchema, CategoryCreateSchema
from db.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/categories', response_model=List[CategorySchema], tags=['category'])
def get_all_categories(db: Session = Depends(get_db)):
    categories = category_crud.get_all_categories(db)
    return categories


@router.post('/categories', response_model=CategorySchema, status_code=status.HTTP_201_CREATED, tags=['category'])
def create_category(category: CategoryCreateSchema,
                    db: Session = Depends(get_db)):
    new_category = category_crud.create_category(category, db)
    return new_category


@router.put('/categories/{category_id}', response_model=CategorySchema, tags=['category'])
def update_category(
        category_id: int,
        changed_category: CategoryCreateSchema,
        db: Session = Depends(get_db),
):
    updated_category = category_crud.update_category(category_id, changed_category, db)
    if updated_category:
        return updated_category
    else:
        raise HTTPException(status_code=404)


@router.get('/categories/{category_id}', response_model=CategorySchema, tags=['category'])
def get_category(
        category_id: int,
        db: Session = Depends(get_db),
):
    category = category_crud.get_category_by_id(category_id, db)
    if not category:
        raise HTTPException(status_code=404)
    return category


@router.delete('/categories/{category_id}', response_model=None, tags=['category'])
def delete_category(
        category_id: int,
        db: Session = Depends(get_db)):
    category_crud.delete_category_by_id(category_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
