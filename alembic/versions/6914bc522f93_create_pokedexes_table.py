"""create_pokedexes_table

Revision ID: 6914bc522f93
Revises:
Create Date: 2016-10-16 17:03:58.272820

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy_searchable import sync_trigger
from sqlalchemy_utils import TSVectorType


# revision identifiers, used by Alembic.
revision = '6914bc522f93'
down_revision = None
branch_labels = None
depends_on = None

searchable = ['name', 'official_name', 'region', 'description']


def upgrade():
    op.create_table(
        'pokedexes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, unique=True, nullable=False),
        sa.Column('official_name', sa.Text, unique=True, nullable=False),
        sa.Column('region', sa.Text, nullable=True, default=None),
        sa.Column('description', sa.Text, nullable=True, default=None),

        sa.Column('search_vector', TSVectorType(searchable)),

        sa.Column('inserted_at', sa.DateTime,
                  default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime,
                  default=sa.func.current_timestamp(),
                  onupdate=sa.func.current_timestamp(), nullable=False)
    )

    conn = op.get_bind()
    sync_trigger(conn, 'pokedexes', 'search_vector', searchable)


def downgrade():
    op.drop_table('pokedexes')
