"""Catalogos inicial

Revision ID: 775ab8905dda
Revises: 6cff19df8e16
Create Date: 2016-08-14 20:49:27.881936

"""

# revision identifiers, used by Alembic.
revision = '775ab8905dda'
down_revision = '6cff19df8e16'
branch_labels = None
depends_on = None

import sys
if "/home/jstitch/src/python" not in sys.path:
    sys.path.append("/home/jstitch/src/python")
import asistenciaInfantiles.schema as schema

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('{}://{}:{}@{}/{}'.format("mysql", "jstitch", "podemos", "localhost", "asistenciaInfantiles"), echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def upgrade():
    for equipo in ["Chiquitos", "Medianos", "Grandes", "KT"]:
        eq = schema.Equipo(equipo)
        session.add(eq)

    for ciclo in [("2015-2016","2015-08-29","2016-06-26")]:
        cic = schema.Ciclo(ciclo[0],ciclo[1],ciclo[2])
        session.add(cic)

    session.commit()


def downgrade():
    ciclos = session.query(schema.Ciclo).all()
    for ciclo in ciclos:
        session.delete(ciclo)
    equipos = session.query(schema.Equipo).all()
    for equipo in equipos:
        session.delete(equipo)
    session.commit()
