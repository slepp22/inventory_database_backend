import logging

from sqlalchemy.orm import Session

from app.api.endpoints.report.schemas import ReportCreateSchema
from db.models import Report


def create_report(schema: ReportCreateSchema, db: Session):
    entity = Report(**schema.dict())
    logging.info('Report created with id {}'.format(entity.id))
    db.add(entity)
    db.commit()
    return entity


def get_report_by_id(report_id: int, db: Session):
    entity = db.query(Report).filter(Report.id == report_id).first()
    return entity


def get_all_reports(db: Session):
    return db.query(Report).all()


def update_report(report_id: int, changed_report: ReportCreateSchema, db: Session):
    report = get_report_by_id(report_id, db)
    if report:
        for key, value in changed_report.dict().items():
            setattr(report, key, value)
        logging.info('Report updated with id {}'.format(report.id))
        db.commit()
        db.refresh(report)
        return report
    else:
        return None
