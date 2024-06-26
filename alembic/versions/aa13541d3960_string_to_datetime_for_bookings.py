"""String to DateTime for Bookings

Revision ID: aa13541d3960
Revises: d28296efa7df
Create Date: 2024-05-01 10:26:30.144338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa13541d3960'
down_revision: Union[str, None] = 'd28296efa7df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    ALTER TABLE bookings
    ALTER COLUMN time_start TYPE TIMESTAMP WITHOUT TIME ZONE
    USING time_start::TIMESTAMP WITHOUT TIME ZONE
    """)
    op.execute("""
    ALTER TABLE bookings
    ALTER COLUMN time_end TYPE TIMESTAMP WITHOUT TIME ZONE
    USING time_end::TIMESTAMP WITHOUT TIME ZONE
    """)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'time_end',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('bookings', 'time_start',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    # ### end Alembic commands ###
