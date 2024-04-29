import logging

from alembic.config import Config
from alembic import command

from app.api.endpoints.db_migration.schemas import TriggerRequestSchema

DB_KEY = "1337"


def trigger_db_migration(request: TriggerRequestSchema):
    if request.key != DB_KEY:
        return {"message": "Invalid Key"}
    else:
        alembic_cfg = "alembic.ini"
        alembic_config = Config(alembic_cfg)
        command.upgrade(alembic_config, "head")
        logging.info("DB Migration Triggered")
        return {"message": "DB Migration Triggered"}
