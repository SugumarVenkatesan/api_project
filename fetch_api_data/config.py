import enum

@enum.unique
class APIList(enum.Enum):
    F1_API = 'http://ergast.com/api/f1/2013/driverStandings.json'
    SOUND_CLOUD_API = 'SOUND_CLOUD_API'
    