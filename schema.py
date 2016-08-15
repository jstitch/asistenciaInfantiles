from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Table, ForeignKey
from sqlalchemy.schema import Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

Base = declarative_base()

class Equipo(Base):
    id     = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre = Column(String(20), index=True, unique=True)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return "<Equipo {}: {}>".format(self.id, self.nombre)


class Ciclo(Base):
    id     = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre = Column(String(10), index=True, unique=True)
    inicio = Column(Date)
    fin    = Column(Date)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return "<Ciclo {}: {}, {} - {}>".format(self.id, self.nombre, self.inicio.strftime('%Y-%d-%m'), self.fin.strftime('%Y-%m-%d'))


class Participante(Base):
    id           = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre       = Column(String(60), index=True)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return "<Participante {}: {}".format(self.id, self.nombre)


class Encuentro(Base):
    id            = Column(Integer, primary_key=True, doc='Llave primaria')
    nombre        = Column(String(20), index=True)
    fecha         = Column(Date, unique=True)
    duracion      = Column(Integer, default=2)

    # participantes = ManyToManyField(Participante, through='Asistencia')

    ciclo_id      = Column(Integer, ForeignKey(Ciclo.id), nullable=False)
    Ciclo         = relationship('Ciclo', backref='encuentros')

    def __str__(self):
        return self.nombre + " " + self.fecha.strftime("%Y")

    def __repr__(self):
        return "<Encuentro {}: {}, ciclo {}, fecha {}, duracion {} dias>".format(self.id, str(self), str(self.Ciclo), self.fecha.strftime('%Y-%m-%d'), self.duracion)


class Asistencia(Base):
    id              = Column(Integer, primary_key=True, doc='Llave primaria')
    telefono        = Column(String(15), nullable=True
    telefono2       = Column(String(15), nullable=True)

    participante_id = Column(Integer, ForeignKey(Participante.id), nullable=False)
    Participante    = relationship('Participante', backref='asistencias')

    encuentro_id    = Column(Integer, ForeignKey(Encuentro.id), nullable=False)
    Encuentro       = relationship('Encuentro', backref='asistencias')

    equipo_id       = Column(Integer, ForeignKey(Equipo.id), nullable=False)
    Equipo          = relationship('Equipo', backref='asistencias')

    Index('idx_asistencia', participante_id, encuentro_id, equipo_id, unique=True)

    def __str__(self):
        return str(self.participante) + ", " + str(self.encuentro) + ", " + str(self.equipo) + ", " + self.telefono

    def __repr__(self):
        return "<Asistencia {}: {}, {} {}, {}, {}".format(self.id, str(self.Participante), str(self.Encuentro), str(self.Encuentro.Ciclo), str(self.Equipo), "telefono{}: {}{}".format("s" if self.telefono2 else "", self.telefono, (", "+self.telefono2) if self.telefono2 else "") if self.telefono)
