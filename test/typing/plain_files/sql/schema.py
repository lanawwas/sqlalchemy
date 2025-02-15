from typing import Union

from sqlalchemy import Constraint
from sqlalchemy import Index
from sqlalchemy import MetaData
from sqlalchemy import Table

MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)


MetaData(naming_convention={"uq": "uq_%(table_name)s_%(column_0_N_name)s"})


def fk_guid(constraint: Union[Constraint, Index], table: Table) -> str:
    return "foo"


MetaData(
    naming_convention={
        "fk_guid": fk_guid,
        "ix": "ix_%(column_0_label)s",
        "fk": "fk_%(fk_guid)s",
        "foo": lambda c, t: t.name + str(c.name),
    }
)
