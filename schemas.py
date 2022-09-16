from pydantic import BaseModel


class CircuitsBase(BaseModel):
    circuitId: int
    circuitRef: str | None = None
    name: str | None = None
    location: str | None = None
    country: str | None = None




class Circuits(CircuitsBase):
    circuitId = int
    circuitRef = str
    name = str
    location = str
    country = str
    lat = float
    lng = float
    alt = int
    url = str

    class Config:
        orm_mode = True


class ConstructorsBase(BaseModel):
    constructorId: int
    constructorRef: str | None = None
    name: str | None = None
    nationality: str | None = None
    # url: str | None = None


class Constructors(ConstructorsBase):
    constructorId = int
    constructorRef = str
    name = str
    nationality = str
    url = str

    class Config:
        orm_mode = True


class DriversBase(BaseModel):
    driverId: int
    driverRef: str | None = None
    number: str | None = None
    code: str | None = None
    name: str | None = None
    dob: str | None = None
    nationality: str | None = None



class Drivers(DriversBase):
    driverId = int
    driverRef = str
    number = str
    code = str
    name = str
    dob = str
    nationality = str
 

    class Config:
        orm_mode = True


class LapTimesBase(BaseModel):
    raceId: int
    driverId: int
    lap: int
    position: int
    time: str | None = None
    milliseconds: str | None = None


class LapTimes(LapTimesBase):
    raceId = int
    driverId = int
    lap = int
    position = int
    time = str
    milliseconds = str

    class Config:
        orm_mode = True


class PitStopsBase(BaseModel):
    raceId: int
    driverId: int
    stop: int
    lap: int
    time: str | None = None
    duration: str | None = None
    milliseconds: int


class PitStops(PitStopsBase):
    raceId = int
    driverId = int
    stop = int
    lap = int
    time = str
    duration = str
    milliseconds = int

    class Config:
        orm_mode = True


class QualifyingBase(BaseModel):
    qualifyId: int
    raceId: int
    driverId: int
    constructorId: int
    number: int
    position: int
    q1: str | None = None
    q2: str | None = None
    q3: str | None = None


class Qualifying(QualifyingBase):
    qualifyId = int
    raceId = int
    driverId = int
    constructorId = int
    number = int
    position = int
    q1 = str
    q2 = str
    q3 = str

    class Config:
        orm_mode = True


class RacesBase(BaseModel):
    year: int



class Races(RacesBase):
    raceId = int
    year = int
    round = int
    circuitId = int
    name = str
    date = str
    time = str
    url = str

    class Config:
        orm_mode = True


class ResultsBase(BaseModel):
    resultId: int
    raceId: int
    driverId: int
    constructorId: int
    number: str | None = None
    grid: int
    position: str | None = None
    positionText: str | None = None
    positionOrder: str | None = None
    points: float | None = None
    laps: int
    time: str | None = None
    milliseconds: str | None = None
    fastestLap: str | None = None
    rank: str | None = None
    fastestLapTime: str | None = None
    fastestLapSpeed: str | None = None
    statusId: int


class Results(ResultsBase):
    resultId = int
    raceId = int
    driverId = int
    constructorId = int
    number = str
    grid = int
    position = str
    positionText = str
    positionOrder = str
    points = float
    laps = int
    time = str
    milliseconds = str
    fastestLap = str
    rank = str
    fastestLapTime = str
    fastestLapSpeed = str
    statusId = int

    class Config:
        orm_mode = True 