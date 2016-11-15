"""create_pokemon_table

Revision ID: b8c0a8ce383c
Revises: 6914bc522f93
Create Date: 2016-10-16 17:41:41.817945

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy_searchable import sync_trigger
from sqlalchemy_utils import TSVectorType


# revision identifiers, used by Alembic.
revision = 'b8c0a8ce383c'
down_revision = '6914bc522f93'
branch_labels = None
depends_on = None

searchable = ['name', 'flavor_text', 'habitat', 'color', 'shape']


def upgrade():
    op.create_table(
        'pokemon',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, unique=True, nullable=False),
        sa.Column('flavor_text', sa.Text, nullable=False),
        sa.Column('habitat', sa.Text, nullable=True, default=None),
        sa.Column('color', sa.Text, nullable=False),
        sa.Column('shape', sa.Text, nullable=False),

        sa.Column('search_vector', TSVectorType(searchable)),

        sa.Column('inserted_at', sa.DateTime,
                  default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime,
                  default=sa.func.current_timestamp(),
                  onupdate=sa.func.current_timestamp(), nullable=False)
    )

    conn = op.get_bind()
    sync_trigger(conn, 'pokemon', 'search_vector', searchable)


def downgrade():
    op.drop_table('pokemon')
