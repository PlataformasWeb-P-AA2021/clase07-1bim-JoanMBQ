from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club
from genera_tablas import Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Carga de los datos de los clubs
data_clubs = open("data/datos_clubs.txt", "r", encoding="utf-8")
# Lectura de los datos de los clubs
clubs = data_clubs.readlines()

for c in clubs:
    club = c.split(";")
    club[-1] = club[-1].strip()
    session.add(Club(nombre=club[0], deporte=club[1], fundacion=club[-1]))

# Obtener todos los registros de la entidad Club
consultaClubs = session.query(Club).all()

# Carga de los datos de los jugadores
data_jugadores = open("data/datos_jugadores.txt", "r", encoding="utf-8")
# Lectura de los datos de los jugadores
jugadores = data_jugadores.readlines()

for j in jugadores:
    jugador = j.split(";")
    jugador[-1] = jugador[-1].strip()
    for club in consultaClubs:
        if(jugador[0] == club.nombre):
            id_club = club.id
    session.add(Jugador(nombre=jugador[3], dorsal=jugador[2], posicion=jugador[1], club_id=id_club))

session.commit()