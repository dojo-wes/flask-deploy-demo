"""empty message

Revision ID: 24fdab907b52
Revises: e1cbcaaaf046
Create Date: 2019-03-13 19:26:45.283848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24fdab907b52'
down_revision = 'e1cbcaaaf046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stuff', sa.String(length=240), nullable=True))
        batch_op.drop_column('content')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.VARCHAR(length=240), nullable=True))
        batch_op.drop_column('stuff')

    # ### end Alembic commands ###
