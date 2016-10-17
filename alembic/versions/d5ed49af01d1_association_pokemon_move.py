"""association_pokemon_move

Revision ID: d5ed49af01d1
Revises: 252d4f1edfbc
Create Date: 2016-10-17 04:18:27.248630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ed49af01d1'
down_revision = '252d4f1edfbc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pokemon_moves',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('pokemon_id', sa.Integer, sa.ForeignKey('pokemon.id')),
        sa.Column('move_id', sa.Integer, sa.ForeignKey('moves.id'))
    )


def downgrade():
    op.drop_table('pokemon_moves')
