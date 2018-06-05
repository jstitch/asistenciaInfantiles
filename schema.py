from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Table, ForeignKey
from sqlalchemy.schema import Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

Base = declarative_base()

class Equipo(Base):
    __tablename__ = "equipos"

    id     = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre = Column(String(20), index=True, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return "<Equipo {}: {}>".format(self.id, self.nombre)


class Ciclo(Base):
    __tablename__ = "ciclos"

    id     = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre = Column(String(10), index=True, unique=True)
    inicio = Column(Date)
    fin    = Column(Date)


    def __init__(self, nombre, inicio, fin):
        self.nombre = nombre
        self.inicio = inicio
        self.fin    = fin

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return "<Ciclo {}: {}, {} - {}>".format(self.id, self.nombre, self.inicio.strftime('%Y-%m-%d'), self.fin.strftime('%Y-%m-%d'))


from asistencias import Session
s = Session()
ciclos = s.query(Ciclo).all()
ciclo_anterior = [ c for c in ciclos if c.inicio == max([ci.inicio for ci in ciclos]) ][0]
class Participante(Base):
    __tablename__ = "participantes"

    id           = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre       = Column(String(60), index=True, unique=True)

    @property
    def asistencias_totales(self):
        return self.asistencias

    @property
    def asistencias_ciclo(self):
        return [ a for a in self.asistencias if a.Encuentro.Ciclo.id == ciclo_anterior.id ]

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return "<Participante {}: {}".format(self.id, self.nombre)


class Encuentro(Base):
    __tablename__ = "encuentros"

    id            = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre        = Column(String(20), index=True)
    fecha         = Column(Date, unique=True)
    duracion      = Column(Integer, default=2)
    alias         = Column(String(20))

    # participantes = ManyToManyField(Participante, through='Asistencia')

    ciclo_id      = Column(Integer, ForeignKey(Ciclo.id), nullable=False)
    Ciclo         = relationship('Ciclo', backref='encuentros')

    def __init__(self, nombre, fecha, duracion, ciclo):
        self.nombre   = nombre
        self.fecha    = fecha
        self.duracion = duracion
        self.ciclo_id = ciclo.id

    def __str__(self):
        return self.nombre + " " + self.fecha.strftime("%Y")

    def __repr__(self):
        return "<Encuentro {}: {}, ciclo {}, fecha {}, duracion {} dias>".format(self.id, str(self), str(self.Ciclo), self.fecha.strftime('%Y-%m-%d'), self.duracion)


class Asistencia(Base):
    __tablename__ = "asistencias"

    id              = Column(Integer, primary_key=True, doc='Llave primaria')
    telefono        = Column(String(15), nullable=True)
    telefono2       = Column(String(15), nullable=True)

    participante_id = Column(Integer, ForeignKey(Participante.id), nullable=False)
    Participante    = relationship('Participante', backref='asistencias')

    encuentro_id    = Column(Integer, ForeignKey(Encuentro.id), nullable=False)
    Encuentro       = relationship('Encuentro', backref='asistencias')

    equipo_id       = Column(Integer, ForeignKey(Equipo.id), nullable=False)
    Equipo          = relationship('Equipo', backref='asistencias')

    Index('idx_asistencia', participante_id, encuentro_id, equipo_id, unique=True)

    def __init__(self, telefono, telefono2, participante, encuentro, equipo):
        self.telefono        = telefono
        self.telefono2       = telefono2
        self.participante_id = participante.id
        self.encuentro_id    = encuentro.id
        self.equipo_id       = equipo.id

    def __str__(self):
        return str(self.participante) + ", " + str(self.encuentro) + ", " + str(self.equipo) + ", " + self.telefono

    def __repr__(self):
        return "<Asistencia {}: {}, {} {}, {}, {}".format(self.id,
                                                          str(self.Participante),
                                                          str(self.Encuentro),
                                                          str(self.Encuentro.Ciclo),
                                                          str(self.Equipo),
                                                          "telefono{}: {}{}".format("s" if self.telefono2 else "",
                                                                                    self.telefono,
                                                                                    (", "+self.telefono2) if self.telefono2 else "") if self.telefono else "")
