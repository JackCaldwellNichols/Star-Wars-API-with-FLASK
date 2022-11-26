"""empty message

Revision ID: 152cf48b1cca
Revises: 64b5a1b00822
Create Date: 2022-11-24 18:47:51.166171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '152cf48b1cca'
down_revision = '64b5a1b00822'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'people', ['name'])
    op.create_unique_constraint(None, 'planets', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'planets', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    # ### end Alembic commands ###