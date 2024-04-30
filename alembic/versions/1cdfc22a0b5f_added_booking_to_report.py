"""Added Booking to Report

Revision ID: 1cdfc22a0b5f
Revises: d8411554e97e
Create Date: 2024-04-30 17:05:48.925150

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cdfc22a0b5f'
down_revision: Union[str, None] = 'd8411554e97e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reports', sa.Column('booking_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'reports', 'bookings', ['booking_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reports', type_='foreignkey')
    op.drop_column('reports', 'booking_id')
    # ### end Alembic commands ###
