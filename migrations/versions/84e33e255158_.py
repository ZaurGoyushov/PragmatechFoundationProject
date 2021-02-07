"""empty message

Revision ID: 84e33e255158
Revises: 5999a556d531
Create Date: 2021-02-07 16:51:04.472117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84e33e255158'
down_revision = '5999a556d531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'brand', ['BrandName'])
    op.create_unique_constraint(None, 'category', ['CategoryName'])
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_constraint(None, 'brand', type_='unique')
    # ### end Alembic commands ###
