"""empty message

Revision ID: e40eb0b52f30
Revises: 88e2be459489
Create Date: 2021-02-07 22:13:00.883308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e40eb0b52f30'
down_revision = '88e2be459489'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('cat_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'products', 'category', ['cat_id'], ['Category_id'])
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'cat_id')
    # ### end Alembic commands ###
