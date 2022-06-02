"""Added pro to user tables

Revision ID: f84123684462
Revises: ce34800b65a1
Create Date: 2022-06-01 15:54:21.661729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f84123684462'
down_revision = 'ce34800b65a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('super', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'super')
    # ### end Alembic commands ###