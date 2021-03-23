"""empty message

Revision ID: bab348af5ace
Revises: 
Create Date: 2021-03-23 11:45:49.157632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bab348af5ace'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('number_of_bedrooms', sa.Float(), nullable=True),
    sa.Column('number_of_bathrooms', sa.Float(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###