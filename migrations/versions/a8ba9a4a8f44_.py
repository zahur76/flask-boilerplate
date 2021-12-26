"""empty message

Revision ID: a8ba9a4a8f44
Revises: ba2eb6fcb753
Create Date: 2021-12-26 10:13:17.365359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ba9a4a8f44'
down_revision = 'ba2eb6fcb753'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###