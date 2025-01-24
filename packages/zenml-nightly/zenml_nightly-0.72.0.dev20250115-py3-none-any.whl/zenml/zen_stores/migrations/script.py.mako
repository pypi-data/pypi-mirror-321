"""${message} [${up_revision}].

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
import sqlmodel
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade database schema and/or data, creating a new revision."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade database schema and/or data back to the previous revision."""
    ${downgrades if downgrades else "pass"}
