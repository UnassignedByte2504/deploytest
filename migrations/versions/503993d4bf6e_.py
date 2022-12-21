"""empty message

Revision ID: 503993d4bf6e
Revises: 
Create Date: 2022-12-20 12:43:19.508188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '503993d4bf6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['country'], ['country.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_type', sa.String(length=80), nullable=True),
    sa.Column('user_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_type'], ['user_type.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('state', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['state'], ['state.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_social_media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('website_url', sa.String(length=80), nullable=True),
    sa.Column('youtube_url', sa.String(length=80), nullable=True),
    sa.Column('soundcloud_url', sa.String(length=80), nullable=True),
    sa.Column('instagram_url', sa.String(length=80), nullable=True),
    sa.Column('facebook_url', sa.String(length=80), nullable=True),
    sa.Column('twitter_url', sa.String(length=80), nullable=True),
    sa.Column('tiktok_url', sa.String(length=80), nullable=True),
    sa.Column('snapchat_url', sa.String(length=80), nullable=True),
    sa.Column('spotify_url', sa.String(length=80), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('facebook_url'),
    sa.UniqueConstraint('instagram_url'),
    sa.UniqueConstraint('snapchat_url'),
    sa.UniqueConstraint('soundcloud_url'),
    sa.UniqueConstraint('spotify_url'),
    sa.UniqueConstraint('tiktok_url'),
    sa.UniqueConstraint('twitter_url'),
    sa.UniqueConstraint('website_url'),
    sa.UniqueConstraint('youtube_url')
    )
    op.create_table('zip_codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zip_code', sa.String(length=80), nullable=False),
    sa.Column('city', sa.String(length=80), nullable=False),
    sa.Column('state', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['cities.name'], ),
    sa.ForeignKeyConstraint(['country'], ['country.name'], ),
    sa.ForeignKeyConstraint(['state'], ['state.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('zip_code')
    )
    op.create_table('user_contact_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(length=80), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('country', sa.String(length=80), nullable=True),
    sa.Column('state', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('zip_code', sa.String(length=80), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['cities.name'], ),
    sa.ForeignKeyConstraint(['country'], ['country.name'], ),
    sa.ForeignKeyConstraint(['state'], ['state.name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['zip_code'], ['zip_codes.zip_code'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_contact_info')
    op.drop_table('zip_codes')
    op.drop_table('user_social_media')
    op.drop_table('cities')
    op.drop_table('user')
    op.drop_table('state')
    op.drop_table('user_type')
    op.drop_table('country')
    # ### end Alembic commands ###