"""Create items table

Revision ID: 1571b66abaf5
Revises: 
Create Date: 2025-08-23 16:18:07.879485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1571b66abaf5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Crear tabla items
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False, index=True),
        sa.Column('price', sa.Float, nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Eliminar tabla items
    op.drop_table('items')
