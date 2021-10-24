"""empty message

Revision ID: 122b0bf6e2b8
Revises: 
Create Date: 2021-10-24 20:58:51.919517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122b0bf6e2b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('category', sa.String(length=45), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=45), nullable=True),
    sa.Column('phone', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=45), nullable=True),
    sa.Column('User_idUser', sa.Integer(), nullable=True),
    sa.Column('Audience_idAudience', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Audience_idAudience'], ['product.id'], ),
    sa.ForeignKeyConstraint(['User_idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('product')
    # ### end Alembic commands ###