"""empty message

Revision ID: f4aecbb18f74
Revises: b11b0b88b13e
Create Date: 2023-11-19 17:38:50.552155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4aecbb18f74'
down_revision: Union[str, None] = 'b11b0b88b13e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sm_overrides',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('flags', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sm_admins_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inherit_order', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['sm_admins.id'], name='fk_sm_admins_groups_sm_admins_admin_id_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['group_id'], ['sm_groups.id'], name='fk_sm_admins_groups_sm_groups_group_id_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('admins_groups')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins_groups',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('admin_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['sm_admins.id'], name='fk_admins_groups_sm_admins_admin_id_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['group_id'], ['sm_groups.id'], name='fk_admins_groups_sm_groups_group_id_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='admins_groups_pkey')
    )
    op.drop_table('sm_admins_groups')
    op.drop_table('sm_overrides')
    # ### end Alembic commands ###
