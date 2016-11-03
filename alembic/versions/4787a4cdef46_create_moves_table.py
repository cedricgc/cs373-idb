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
        sa.Column('name', sa.Text, unique=True, nullable=False),
        sa.Column('flavor_text', sa.Text, nullable=True, default=None),
        sa.Column('short_effect', sa.Text, nullable=False),
        sa.Column('effect', sa.Text, nullable=False),
        sa.Column('damage_class', sa.Text, nullable=True, default=None),
        sa.Column('power_points', sa.Integer, nullable=True, default=None),
        sa.Column('power', sa.Integer, nullable=True, default=None),
        sa.Column('accuracy', sa.Integer, nullable=True, default=None),

        sa.Column('inserted_at', sa.DateTime,
                  default=sa.func.current_timestamp(), nullable=False),
        sa.Column('updated_at', sa.DateTime,
                  default=sa.func.current_timestamp(),
                  onupdate=sa.func.current_timestamp(), nullable=False)
    )


def downgrade():
    op.drop_table('moves')
