"""Catalogo encuentros

Revision ID: e1665f7b3aed
Revises: 775ab8905dda
Create Date: 2016-08-14 21:09:54.754025

"""

# revision identifiers, used by Alembic.
revision = 'e1665f7b3aed'
down_revision = '775ab8905dda'
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
    ciclo = session.query(schema.Ciclo).filter(schema.Ciclo.nombre=="2015-2016").one()
    for encuentro in [("Septiembre" , "2015-09-12" , 2) ,
                      ("Octubre"    , "2015-10-17" , 2) ,
                      ("Noviembre"  , "2015-11-14" , 2) ,
                      ("Diciembre"  , "2015-12-12" , 2) ,
                      ("Enero"      , "2016-01-16" , 2) ,
                      ("Febrero"    , "2016-02-20" , 2) ,
                      ("Marzo"      , "2016-03-19" , 2) ,
                      ("Abril"      , "2016-04-23" , 2) ,
                      ("Mayo"       , "2016-05-21" , 2) ,
                      ("Junio"      , "2016-06-18" , 2) ,
                     ]:
        enc = schema.Encuentro(encuentro[0], encuentro[1], encuentro[2], ciclo)
        session.add(enc)

    session.commit()


def downgrade():
    encuentros = session.query(schema.Encuentro).all()
    for encuentro in encuentros:
        session.delete(encuentro)
    session.commit()
