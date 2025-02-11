"""delete email from send_emails

Revision ID: 17d613986bc2
Revises: bd7cb053d1a9
Create Date: 2024-07-14 20:23:24.822888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17d613986bc2'
down_revision = 'bd7cb053d1a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('send_emails', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('send_emails', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
