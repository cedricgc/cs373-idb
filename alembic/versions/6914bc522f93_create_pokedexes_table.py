"""create_pokedexes_table

Revision ID: 6914bc522f93
Revises:
Create Date: 2016-10-16 17:03:58.272820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6914bc522f93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pokedexes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('official_name', sa.Text, nullable=False),
        sa.Column('region', sa.Text, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
    )


def downgrade():
    op.drop_table('pokedexes')
