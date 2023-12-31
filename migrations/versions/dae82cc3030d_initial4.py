"""initial4

Revision ID: dae82cc3030d
Revises: 5ccd5062b53d
Create Date: 2023-07-16 22:39:06.814207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dae82cc3030d'
down_revision = '5ccd5062b53d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.drop_column('user', 'is_super')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_super', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_superuser')
    # ### end Alembic commands ###
