from sqlalchemy import  Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Circuits(Base):
    __tablename__ = "circuits"

    circuitId = Column(Integer, ForeignKey("circuit.circuitid"), primary_key=True, index=True)
    circuitRef = Column(String)
    name = Column(String)
    location = Column(String)
    country = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(String)
    url = Column(String)

    CIRCUITS = relationship("results", back_populates="circuits")


class Constructors(Base):
    __tablename__ = "constructors"

    constructorId = Column(Integer, ForeignKey("constructors.constructorid"), primary_key=True, index=True)
    constructorRef = Column(String)
    name = Column(String)
    nationality = Column(Integer, )

    CONSTRUCTORS = relationship("results", back_populates="constructors")


class Drivers(Base):
    __tablename__ = "drivers"

    driverId = Column(Integer, ForeignKey("drivers.driverid"), primary_key=True, index=True)
    driverRef = Column(String)
    number = Column(String)
    code = Column(String)
    name_forename = Column(String)
    name_surname = Column(String)
    dob = Column(String)
    nationality = Column(String)
    url = Column(String)

    DRIVERS = relationship("results", back_populates="drivers")


class Lap_Times(Base):
    __tablename__ = "lap_times"

    raceId = Column(Integer, ForeignKey("lap_times.raceid"), primary_key=True, index=True)
    driverid = Column(Integer)
    lap = Column(Integer)
    position = Column(Integer)
    time = Column(String)
    milliseconds = Column(Integer)

    LAP_TIMES = relationship("results", back_populates="lap_times")


class Pit_Stops(Base):
    __tablename__ = "pit_stops"

    raceId = Column(Integer, ForeignKey("pit_stops.raceid"), primary_key=True, index=True)
    driverid = Column(Integer)
    stop = Column(Integer)
    lap = Column(Integer)
    time = Column(String)
    duration = Column(Float)
    milliseconds = Column(Integer)

    PIT_STOPS = relationship("results", back_populates="pit_stops")


class Qualifying(Base):
    __tablename__ = "qualifying"

    qualifyingId = Column(Integer) 
    raceId = Column(Integer, ForeignKey("qualifying.raceid"), primary_key=True, index=True)
    driverId = Column(Integer)
    constructorId = Column(Integer)
    number = Column(Integer)
    position = Column(Integer)
    q1 = Column(String)
    q2 = Column(String)
    q3 = Column(String)

    DRIVERS = relationship("results", back_populates="qualifying")

class Races(Base):
    __tablename__ = "races"

    raceId = Column(Integer) 
    year = Column(Integer, ForeignKey("qualifying.raceid"), primary_key=True, index=True)
    round = Column(Integer)
    circuitId = Column(Integer)
    name = Column(String)
    date = Column(String)
    time = Column(String)
    url = Column(String)

    DRIVERS = relationship("results", back_populates="races")

class Results(Base):
    __tablename__ = "results"

    resultId = Column(Integer, primary_key=True, index=True)
    raceId = Column(Integer, ForeignKey("qualifying.raceid"))
    driverId = Column(Integer)
    constructorId = Column(Integer)
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionText = Column(String)
    positionOrder = Column(Integer)
    points = Column(Integer)
    laps = Column(Integer)
    time = Column(String)
    milliseconds = Column(Integer)
    fastestLapTime = Column(String)
    fastestLapSpeed = Column(Float)
    statusId = Column(Integer)

    DRIVERS = relationship("results", back_populates="qualifying")