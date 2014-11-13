"""empty message

Revision ID: 4ee2f6d9d214
Revises: None
Create Date: 2014-11-08 14:58:54.192819

"""

# revision identifiers, used by Alembic.
revision = '4ee2f6d9d214'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'author_id')
    ### end Alembic commands ###