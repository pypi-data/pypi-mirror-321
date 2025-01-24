"""Add model version producer run unique constraint [a1237ba94fd8].

Revision ID: a1237ba94fd8
Revises: 26351d482b9e
Create Date: 2024-12-13 10:28:55.432414

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "a1237ba94fd8"
down_revision = "26351d482b9e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade database schema and/or data, creating a new revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("model_version", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "producer_run_id_if_numeric",
                sqlmodel.sql.sqltypes.GUID(),
                nullable=True,
            )
        )

    # Set the producer_run_id_if_numeric column to the model version ID for
    # existing rows
    connection = op.get_bind()
    metadata = sa.MetaData()
    metadata.reflect(only=("model_version",), bind=connection)
    model_version_table = sa.Table("model_version", metadata)

    connection.execute(
        model_version_table.update().values(
            producer_run_id_if_numeric=model_version_table.c.id
        )
    )

    with op.batch_alter_table("model_version", schema=None) as batch_op:
        batch_op.alter_column(
            "producer_run_id_if_numeric",
            existing_type=sqlmodel.sql.sqltypes.GUID(),
            nullable=False,
        )
        batch_op.create_unique_constraint(
            "unique_numeric_version_for_pipeline_run",
            ["model_id", "producer_run_id_if_numeric"],
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade database schema and/or data back to the previous revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("model_version", schema=None) as batch_op:
        batch_op.drop_constraint(
            "unique_numeric_version_for_pipeline_run", type_="unique"
        )
        batch_op.drop_column("producer_run_id_if_numeric")

    # ### end Alembic commands ###
