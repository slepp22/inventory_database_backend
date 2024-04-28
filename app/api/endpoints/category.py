from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import category as category_model
from db.config import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/categories", response_model=list[category_model.Category])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(category_model.Category).all()
    return categories


@router.get("/categories/{category_id}", response_model=category_model.Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/categories", response_model=category_model.Category)
def create_category(name: str, db: Session = Depends(get_db)):
    category = category_model.Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.put("/categories/{category_id}", response_model=category_model.Category)
def update_category(category_id: int, name: str, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    category.name = name
    db.commit()
    db.refresh(category)
    return category


@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message": "Category deleted successfully"}
