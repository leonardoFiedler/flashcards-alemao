"""create flashcard table

Revision ID: 2efa96021f5e
Revises: 
Create Date: 2025-05-03 13:05:48.420577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2efa96021f5e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    # Name of the category. It can be custom or based on a context
    # z.b. house words, basic verbs...
    op.create_table(
        'category',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('name', sa.VARCHAR(100), nullable=False),
        sa.Column("timestamp", sa.TIMESTAMP, server_default=sa.func.now())
    )
    
    # Word type actual: Verbs and Nouns
    op.create_table(
        'word_type',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('name', sa.VARCHAR(100), nullable=False),
        sa.Column("timestamp", sa.TIMESTAMP, server_default=sa.func.now())
    )
    
    op.create_index(op.f("ix_word_type_name"), "word_type", ["name"], unique=True)
    
    op.create_table(
        'flashcard',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('id_category', sa.BigInteger, nullable=False),
        sa.Column('id_word_type', sa.BigInteger, nullable=False),
        sa.Column('ge_translation', sa.VARCHAR(300), nullable=False),
        sa.Column('pt_translation', sa.VARCHAR(300), nullable=False),
        sa.Column('image_path', sa.VARCHAR(500), nullable=True),
        sa.Column('tip', sa.VARCHAR(500), nullable=True),
        sa.Column('article', sa.VARCHAR(8), nullable=True),
        sa.Column('plural', sa.VARCHAR(300), nullable=True),
        sa.Column('plural_options', sa.VARCHAR(500), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_category"],
            ["category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["id_word_type"],
            ["word_type.id"],
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
