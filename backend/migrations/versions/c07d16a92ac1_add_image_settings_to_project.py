"""add image settings to project

Revision ID: c07d16a92ac1
Revises: 38292967f3ca
Create Date: 2026-01-08 23:59:55.112012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c07d16a92ac1'
down_revision = '38292967f3ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add image_resolution and image_aspect_ratio columns to projects table
    op.add_column('projects', sa.Column('image_resolution', sa.String(10), nullable=True, server_default='2K'))
    op.add_column('projects', sa.Column('image_aspect_ratio', sa.String(10), nullable=True, server_default='16:9'))


def downgrade() -> None:
    # Remove image_resolution and image_aspect_ratio columns
    op.drop_column('projects', 'image_aspect_ratio')
    op.drop_column('projects', 'image_resolution')



