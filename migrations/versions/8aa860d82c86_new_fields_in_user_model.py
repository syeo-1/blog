"""new fields in user model

Revision ID: 8aa860d82c86
Revises: a730a3bc8a9b
Create Date: 2024-12-31 15:38:59.987097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aa860d82c86'
down_revision = 'a730a3bc8a9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
