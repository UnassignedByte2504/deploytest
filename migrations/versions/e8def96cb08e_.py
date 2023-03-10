"""empty message

Revision ID: e8def96cb08e
Revises: 
Create Date: 2023-01-18 13:04:29.427586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8def96cb08e'
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
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name')
    )
    op.create_table('music_genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('musical_instruments_category',
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
    op.create_table('influence_band',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('genre', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['genre'], ['music_genre.name'], ),
    sa.PrimaryKeyConstraint('id')
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
    sa.Column('profile_img', sa.Unicode(), nullable=True),
    sa.Column('portrait_img', sa.Unicode(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_musician', sa.Boolean(), nullable=False),
    sa.Column('is_logged', sa.Boolean(), nullable=False),
    sa.Column('unread_messages', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_type'], ['user_type.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('state', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['state'], ['state.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('direct_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('message_body', sa.String(length=500), nullable=False),
    sa.Column('readed', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('logged_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('login_timestamp', sa.DateTime(), nullable=False),
    sa.Column('logout_timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_ip', sa.String(length=80), nullable=False),
    sa.Column('user_agent', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_feed_back',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('youtube_media1', sa.String(length=255), nullable=True),
    sa.Column('youtube_media2', sa.String(length=255), nullable=True),
    sa.Column('spotify_media1', sa.String(length=255), nullable=True),
    sa.Column('spotify_media2', sa.String(length=255), nullable=True),
    sa.Column('soundcloud_media1', sa.String(length=255), nullable=True),
    sa.Column('soundcloud_media2', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('user_musician_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('artistic_name', sa.String(length=80), nullable=True),
    sa.Column('musical_instruments_other', sa.String(length=80), nullable=True),
    sa.Column('musical_genres_other', sa.String(length=80), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
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
    op.create_table('bands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.Column('music_genre_id', sa.String(length=120), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['music_genre_id'], ['music_genre.name'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user_musician_info.user_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name')
    )
    op.create_table('local',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('local_img', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('ubicacion_local', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_contact_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(length=80), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('country', sa.Integer(), nullable=True),
    sa.Column('state', sa.Integer(), nullable=True),
    sa.Column('city', sa.Integer(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['country'], ['country.id'], ),
    sa.ForeignKeyConstraint(['state'], ['state.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('user_music_genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_musician_info_id', sa.Integer(), nullable=False),
    sa.Column('music_genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['music_genre_id'], ['music_genre.id'], ),
    sa.ForeignKeyConstraint(['user_musician_info_id'], ['user_musician_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_musical_instrument',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_musician_info_id', sa.Integer(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_musician_info_id'], ['user_musician_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('band_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('band_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['bands.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['user_musician_info.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('local_music_genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('musicgenre_id', sa.Integer(), nullable=False),
    sa.Column('local_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['local_id'], ['local.id'], ),
    sa.ForeignKeyConstraint(['musicgenre_id'], ['music_genre.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('musical_instrument',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('musical_instruments_category_id', sa.Integer(), nullable=False),
    sa.Column('user_musical_instruments_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['musical_instruments_category_id'], ['musical_instruments_category.id'], ),
    sa.ForeignKeyConstraint(['user_musical_instruments_id'], ['user_musical_instrument.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('musical_instrument')
    op.drop_table('local_music_genre')
    op.drop_table('band_members')
    op.drop_table('user_musical_instrument')
    op.drop_table('user_music_genre')
    op.drop_table('user_contact_info')
    op.drop_table('local')
    op.drop_table('bands')
    op.drop_table('user_social_media')
    op.drop_table('user_musician_info')
    op.drop_table('user_media')
    op.drop_table('user_feed_back')
    op.drop_table('logged_users')
    op.drop_table('followers')
    op.drop_table('direct_message')
    op.drop_table('city')
    op.drop_table('user')
    op.drop_table('state')
    op.drop_table('influence_band')
    op.drop_table('user_type')
    op.drop_table('musical_instruments_category')
    op.drop_table('music_genre')
    op.drop_table('event')
    op.drop_table('country')
    # ### end Alembic commands ###
