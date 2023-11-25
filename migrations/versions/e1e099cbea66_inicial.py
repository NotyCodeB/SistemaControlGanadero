"""inicial

Revision ID: e1e099cbea66
Revises: 
Create Date: 2023-11-24 13:05:26.638070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1e099cbea66'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=200), nullable=True),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('role', sa.Enum('ganadero', 'admin', name='roletype'), server_default='ganadero', nullable=False),
    sa.Column('cedula', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('ganado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Metodo_identificacion', sa.String(length=120), nullable=True),
    sa.Column('categoria', sa.Enum('leche', 'engorde', name='categoria'), nullable=False),
    sa.Column('genero', sa.Enum('macho', 'hembra', name='genero'), nullable=False),
    sa.Column('litros_leche_diarios', sa.Float(), nullable=False),
    sa.Column('peso', sa.String(length=20), nullable=True),
    sa.Column('registrada_en', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usuario'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Metodo_identificacion')
    )
    op.create_table('vacunaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('carbon', sa.Boolean(), nullable=True),
    sa.Column('fiebre_aftosa', sa.Boolean(), nullable=True),
    sa.Column('bruselosis', sa.Boolean(), nullable=True),
    sa.Column('rabia', sa.Boolean(), nullable=True),
    sa.Column('vitaminas', sa.Boolean(), nullable=True),
    sa.Column('animal', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['animal'], ['ganado.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacunaciones')
    op.drop_table('ganado')
    op.drop_table('users')
    # ### end Alembic commands ###