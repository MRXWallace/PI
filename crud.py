from sqlalchemy.orm import Session
import schemas, models
from sqlalchemy import func



# Año con más carreras
# races['year'].value_counts()
def get_year_more_races(db: Session, rounds: int):
    return '2021'

    # Year_more_races
def get_year_more_races(db: Session, rounds: int):
    return db.query(models.Races).filter(models.Races.round == rounds).first()


# Driver_most_first_places
def get_driver_most_1_places(db: Session, driverId: int):
    return db.query(models.Drivers).filter(models.Drivers.driverId == driverId).first()


# Most traveled circuit
def get_most_traveled_circuit(db: Session, circuitId: int):
    return db.query(models.Circuits).filter(models.Circuits.circuitId == circuitId).first()