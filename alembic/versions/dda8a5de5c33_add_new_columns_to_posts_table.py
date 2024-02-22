"""add new columns to posts table

Revision ID: dda8a5de5c33
Revises: c73225a7c792
Create Date: 2024-02-20 10:50:41.042203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dda8a5de5c33'
down_revision: Union[str, None] = 'c73225a7c792'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
