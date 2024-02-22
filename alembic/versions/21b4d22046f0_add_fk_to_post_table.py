"""add fk to post table

Revision ID: 21b4d22046f0
Revises: 709753992c8b
Create Date: 2024-02-20 13:33:02.234460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21b4d22046f0'
down_revision: Union[str, None] = '709753992c8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False)),
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_suers_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
