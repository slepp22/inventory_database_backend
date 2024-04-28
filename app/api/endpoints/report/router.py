from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session

import app.api.endpoints.report.CRUD as report_crud
from app.api.endpoints.report.schemas import ReportSchema, ReportCreateSchema
from db.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/reports', response_model=List[ReportSchema], tags=['report'])
def get_all_reports(db: Session = Depends(get_db)):
    reports = report_crud.get_all_reports(db)
    return reports


@router.get('/reports/{report_id}', response_model=ReportSchema, tags=['report'])
def get_report_by_id(report_id: int, db: Session = Depends(get_db)):
    report = report_crud.get_report_by_id(report_id, db)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report


@router.post('/reports', response_model=ReportSchema, status_code=201, tags=['report'])
def create_report(report: ReportCreateSchema, db: Session = Depends(get_db)):
    new_report = report_crud.create_report(report, db)
    return new_report


@router.put('/reports/{report_id}', response_model=ReportSchema, tags=['report'])
def update_report(
        report_id: int,
        changed_report: ReportCreateSchema,
        db: Session = Depends(get_db),
):
    updated_report = report_crud.update_report(report_id, changed_report, db)
    if updated_report:
        return updated_report
    else:
        raise HTTPException(status_code=404, detail="Report not found")
