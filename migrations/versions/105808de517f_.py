"""empty message

Revision ID: 105808de517f
Revises: a44f976f39b0
Create Date: 2021-01-27 01:08:48.787721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '105808de517f'
down_revision = 'a44f976f39b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'products', 'category', ['cat_id'], ['Category_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    # ### end Alembic commands ###
