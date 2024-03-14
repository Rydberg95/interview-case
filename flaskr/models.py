from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flaskr.extensions import db


def create_database_tables(app):
    # Creating database tables that do not exist (does not overwrite/recreate if table exist)
    with app.app_context():
        db.create_all()


class Base(DeclarativeBase):
    pass


class InsuranceClaim(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    claim_reference: Mapped[str] = mapped_column(unique=True)
    claim_cost: Mapped[float]
