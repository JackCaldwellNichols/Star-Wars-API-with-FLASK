"""empty message

Revision ID: d52ad763c0bf
Revises: 04333c8055a5
Create Date: 2022-11-23 15:30:38.076153

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd52ad763c0bf'
down_revision = '04333c8055a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourite planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favourite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourite',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('people_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planet_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], name='favourite_ibfk_1'),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], name='favourite_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favourite_ibfk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('favourite planet')
    # ### end Alembic commands ###
