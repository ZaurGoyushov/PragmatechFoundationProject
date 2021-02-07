"""empty message

Revision ID: d1c5bd130c30
Revises: fdba8843e52c
Create Date: 2021-01-27 01:11:58.810899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1c5bd130c30'
down_revision = 'fdba8843e52c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'CategoryName')
    op.create_foreign_key(None, 'products', 'category', ['cat_id'], ['Category_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.add_column('category', sa.Column('CategoryName', sa.TEXT(length=30), nullable=False))
    # ### end Alembic commands ###
