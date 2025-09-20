"""Add sample data

Revision ID: 2a86dbf567c0
Revises: 1571b66abaf5
Create Date: 2025-08-23 16:18:38.341123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a86dbf567c0'
down_revision: Union[str, Sequence[str], None] = '1571b66abaf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Crear tabla temporal para insertar datos
    items_table = sa.table(
        'items',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String),
        sa.column('price', sa.Float)
    )
    
    # Insertar datos de prueba
    op.bulk_insert(
        items_table,
        [
            {'name': 'Laptop', 'price': 999.99},
            {'name': 'Mouse', 'price': 29.99},
            {'name': 'Teclado', 'price': 79.99},
            {'name': 'Monitor', 'price': 299.99},
            {'name': 'Auriculares', 'price': 149.99}
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Eliminar los datos de prueba
    op.execute("DELETE FROM items WHERE name IN ('Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares')")
