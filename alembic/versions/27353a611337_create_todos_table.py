"""create todos table

Revision ID: 27353a611337
Revises: ad1c380734f8
Create Date: 2025-06-13 09:12:35.957268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27353a611337'
down_revision: Union[str, None] = 'ad1c380734f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.execute("""
     create table if todos(
         id bigserial primary key,
         name text,
         completed boolean not null default false
     )
     """)

def downgrade():
     op.execute("drop table todos;")
