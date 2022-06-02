"""Added pro to user tables

Revision ID: ce34800b65a1
Revises: 1632c6afc0fd
Create Date: 2022-06-01 15:53:01.267352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce34800b65a1'
down_revision = '1632c6afc0fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pro', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pro')
    # ### end Alembic commands ###