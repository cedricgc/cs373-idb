"""create_pokemon_table

Revision ID: b8c0a8ce383c
Revises: 6914bc522f93
Create Date: 2016-10-16 17:41:41.817945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c0a8ce383c'
down_revision = '6914bc522f93'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pokemon',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('flavor_text', sa.Text, nullable=False),
        sa.Column('habitat', sa.Text, nullable=False),
        sa.Column('color', sa.Text, nullable=False),
        sa.Column('shape', sa.Text, nullable=False)
    )


def downgrade():
    op.drop_table('pokemon')
