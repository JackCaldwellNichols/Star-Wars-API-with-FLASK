"""empty message

Revision ID: 728518141a54
Revises: d42b9242ac27
Create Date: 2022-11-23 09:09:18.757426

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '728518141a54'
down_revision = 'd42b9242ac27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('terrain', sa.String(length=15), nullable=False))
    op.drop_column('planets', 'description')
    op.drop_column('planets', 'mass')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('mass', mysql.VARCHAR(length=15), nullable=False))
    op.add_column('planets', sa.Column('description', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('planets', 'terrain')
    # ### end Alembic commands ###