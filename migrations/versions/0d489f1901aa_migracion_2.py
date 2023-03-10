"""Migracion 2

Revision ID: 0d489f1901aa
Revises: 3e4065bd8f4e
Create Date: 2023-01-21 11:03:40.212909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d489f1901aa'
down_revision = '3e4065bd8f4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=45), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias')
    # ### end Alembic commands ###
