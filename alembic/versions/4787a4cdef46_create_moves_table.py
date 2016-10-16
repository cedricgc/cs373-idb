"""create_moves_table

Revision ID: 4787a4cdef46
Revises: b8c0a8ce383c
Create Date: 2016-10-16 17:56:15.296732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4787a4cdef46'
down_revision = 'b8c0a8ce383c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'moves',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('flavor_text', sa.Text, nullable=False),
        sa.Column('short_effect', sa.Text, nullable=False),
        sa.Column('effect', sa.Text, nullable=False),
        sa.Column('damage_class', sa.Text, nullable=False),
        sa.Column('power_points', sa.Integer, nullable=False),
        sa.Column('power', sa.Integer, nullable=False),
        sa.Column('accuracy', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('moves')
