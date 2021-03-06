"""empty message

Revision ID: 28ccc9a34fd
Revises: 2eea308400d
Create Date: 2015-10-05 19:45:54.024163

"""

# revision identifiers, used by Alembic.
revision = '28ccc9a34fd'
down_revision = '2eea308400d'

from alembic import op
import sqlalchemy as sa
import citext
from sqlalchemy.sql import table, column

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    data_table = table('forum_boards',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('slug', sa.String(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True)
        # sa.PrimaryKeyConstraint('id'),
        # sa.UniqueConstraint('slug')
    )

    op.bulk_insert(data_table,
        [
            {'id':1, 'name':'General Discussion',            'slug':'general-discussion',
                'description': 'General discussion - Talk about whatever catches your interest!'},
            {'id':2, 'name':'Source Requests',               'slug':'source-requests',
                'description': 'Request new feeds, sources or even new site-features.'},
            {'id':3, 'name':'Site and Release issues', 'slug':'release-errors',
                'description': 'Something broken? Report it here.'},
        ]
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
