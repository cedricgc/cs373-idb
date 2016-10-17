"""association_pokedex_pokemon

Revision ID: 252d4f1edfbc
Revises: 4787a4cdef46
Create Date: 2016-10-17 04:05:56.979687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '252d4f1edfbc'
down_revision = '4787a4cdef46'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pokedex_pokemon',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('pokedex_id', sa.Integer, sa.ForeignKey('pokedexes.id')),
        sa.Column('pokemon_id', sa.Integer, sa.ForeignKey('pokemon.id'))
    )


def downgrade():
    op.drop_table('pokedex_pokemon')
