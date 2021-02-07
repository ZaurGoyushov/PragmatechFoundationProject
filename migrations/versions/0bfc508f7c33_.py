"""empty message

Revision ID: 0bfc508f7c33
Revises: a5fe2c0bc55b
Create Date: 2021-02-07 16:05:50.643404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bfc508f7c33'
down_revision = 'a5fe2c0bc55b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'category', 'brand', ['brand_id'], ['Brand_id'])
    op.add_column('products', sa.Column('cat_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'products', 'category', ['cat_id'], ['Category_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'cat_id')
    op.drop_constraint(None, 'category', type_='foreignkey')
    # ### end Alembic commands ###
