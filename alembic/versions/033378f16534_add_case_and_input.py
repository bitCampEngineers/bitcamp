"""Add Case and Input

Revision ID: 033378f16534
Revises: 5edc4d15799f
Create Date: 2024-06-05 19:06:56.125582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '033378f16534'
down_revision: Union[str, None] = '5edc4d15799f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('input',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_input_id'), 'input', ['id'], unique=False)
    op.create_table('cases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('input_id', sa.Integer(), nullable=True),
    sa.Column('output', sa.String(), nullable=True),
    sa.Column('input_type', sa.String(), nullable=True),
    sa.Column('output_type', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['input_id'], ['input.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cases_id'), 'cases', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cases_id'), table_name='cases')
    op.drop_table('cases')
    op.drop_index(op.f('ix_input_id'), table_name='input')
    op.drop_table('input')
    # ### end Alembic commands ###
