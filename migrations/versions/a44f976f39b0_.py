"""empty message

Revision ID: a44f976f39b0
Revises: 425b097ddb7f
Create Date: 2021-01-27 01:07:24.506205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a44f976f39b0'
down_revision = '425b097ddb7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('Brand', sa.String(length=80), nullable=False))
    op.create_foreign_key(None, 'products', 'category', ['cat_id'], ['Category_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('category', 'Brand')
    # ### end Alembic commands ###