"""empty message

Revision ID: d4b0a996d48b
Revises: 87184056860d
Create Date: 2022-11-23 06:56:01.562971

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd4b0a996d48b'
down_revision = '87184056860d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_index('description', table_name='planets')
    op.drop_index('description_2', table_name='planets')
    op.drop_index('name', table_name='planets')
    op.drop_index('name_2', table_name='planets')
    op.drop_table('planets')
    op.add_column('people', sa.Column('height', sa.String(length=15), nullable=False))
    op.add_column('people', sa.Column('mass', sa.String(length=15), nullable=False))
    op.drop_index('homeworld', table_name='people')
    op.drop_index('homeworld_2', table_name='people')
    op.drop_index('name', table_name='people')
    op.drop_index('name_2', table_name='people')
    op.drop_column('people', 'homeworld')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('homeworld', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('name_2', 'people', ['name'], unique=False)
    op.create_index('name', 'people', ['name'], unique=False)
    op.create_index('homeworld_2', 'people', ['homeworld'], unique=False)
    op.create_index('homeworld', 'people', ['homeworld'], unique=False)
    op.drop_column('people', 'mass')
    op.drop_column('people', 'height')
    op.create_table('planets',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name_2', 'planets', ['name'], unique=False)
    op.create_index('name', 'planets', ['name'], unique=False)
    op.create_index('description_2', 'planets', ['description'], unique=False)
    op.create_index('description', 'planets', ['description'], unique=False)
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###