"""empty message

Revision ID: abc60c0f3cc5
Revises: 8c91499d1552
Create Date: 2021-01-27 00:43:58.134580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abc60c0f3cc5'
down_revision = '8c91499d1552'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('Category_id', sa.Integer(), nullable=False))
    op.drop_column('category', 'id')
    op.add_column('products', sa.Column('Category_Id', sa.Integer(), nullable=False))
    op.add_column('products', sa.Column('ProductImage', sa.String(length=120), nullable=False))
    op.add_column('products', sa.Column('Product_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'products', 'category', ['Category_Id'], ['Category_id'])
    op.drop_column('products', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'Product_id')
    op.drop_column('products', 'ProductImage')
    op.drop_column('products', 'Category_Id')
    op.add_column('category', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_column('category', 'Category_id')
    # ### end Alembic commands ###