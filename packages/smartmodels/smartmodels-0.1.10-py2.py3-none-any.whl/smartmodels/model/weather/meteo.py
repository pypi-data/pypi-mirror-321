from typing import Optional

from agptools.helpers import I
from syncmodels.definitions import UID_TYPE
from syncmodels.mapper import Mapper
from syncmodels.model import BaseModel, Enum, Field
from syncmodels.model.model import Datetime



class ObservationData(BaseModel):
    """

    Pending of integration / discarding

    meta['campos']
    [

      # agp: not observed
     {'id': 'pliqtp',
      'descripcion': 'Precipitación líquida acumulada durante los 60 minutos '
                     'anteriores a la hora indicada por el período de observación '
                     "'datetime' (mm, equivalente a l/m2)",
      'tipo_datos': 'float',
      'requerido': False},

      # agp: not observed
     {'id': 'psolt',
      'descripcion': 'Precipitación sólida acumulada durante los 60 minutos '
                     'anteriores a la hora indicada por el período de observación '
                     "'datetime' (mm, equivalente a l/m2)",
      'tipo_datos': 'float',
      'requerido': False},

      # agp: ignore sky stations  ...
     {'id': 'geo700',
      'descripcion': 'Altura del nivel de la superficie de referencia barométrica '
                     'de 700 hPa calculado para las estaciones con altitud mayor '
                     'de 2300 metros y correspondiente a la fecha indicada por '
                     "'datetime' (m geopotenciales)",
      'tipo_datos': 'float',
      'requerido': False},
     {'id': 'geo850',
      'descripcion': 'Altura del nivel de la superficie de referencia barométrica '
                     'de 850 hPa calculado para las estaciones con altitud mayor '
                     'de 1000 metros y menor o igual a 2300 metros y '
                     "correspondiente a la fecha indicada por 'datetime' (m "
                     'geopotenciales)',
      'tipo_datos': 'float',
      'requerido': False},
     {'id': 'geo925',
      'descripcion': 'Altura del nivel de la superficie barométrica de 925 hPa '
                     'calculado para las estaciones con altitud mayor de 750 '
                     'metros y y menor o igual a 1000 metros correspondiente a la '
                     "fecha indicada por 'datetime' (m geopotenciales)",
      'tipo_datos': 'float',
      'requerido': False},


    """

    id: UID_TYPE = Field(
        description="Indicativo climatógico de la estación meteorológia",
    )
    # TODO: use more 'normalized' names based on meta-info provided by AEMET

    # geospatial
    # geometry: Point
    altitude: Optional[float] = Field(
        None,
        description="Altitud de la estación en metros",
    )

    # location
    ubication: str = Field(
        description="Ubicación de la estación o Nombre de la estación"
    )

    # time
    datetime: Optional[Datetime] = Field(
        description="Fecha hora final del período de observación, se trata de "
        "datos del periodo de la hora anterior a la indicada por este "
        "campo (hora UTC)",
        # pattern=r"\d+\-\d+\-\d+T\d+:\d+:\d+",  # is already a datetime
    )

    # rain
    precipitation: Optional[float] = Field(
        None,
        description="Precipitación acumulada, medida por el pluviómetro, durante "
        "los 60 minutos anteriores a la hora indicada por el período "
        "de observación 'datetime' (mm, equivalente a l/m2)",
    )
    precipitation_disdrometer: Optional[float] = Field(
        None,
        description="Precipitación acumulada, medida por el disdrómetro, durante "
        "los 60 minutos anteriores a la hora indicada por el período "
        "de observación 'datetime' (mm, equivalente a l/m2)",
    )
    # air
    air_temperature: Optional[float] = Field(
        None,
        description="Temperatura instantánea del aire correspondiente a la fecha "
        "dada por 'datetime' (grados Celsius)",
    )
    air_temperature_max: Optional[float] = Field(
        None,
        description="Temperatura máxima del aire, valor máximo de los 60 valores "
        "instantáneos de 'air_temperature' medidos en el período de 60 minutos "
        "anteriores a la hora indicada por el período de observación "
        "'datetime' (grados Celsius)",
    )
    air_temperature_min: Optional[float] = Field(
        None,
        description="Temperatura mínima del aire, valor mínimo de los 60 valores "
        "instantáneos de 'air_temperature' medidos en el período de 60 minutos "
        "anteriores a la hora indicada por el período de observación "
        "'datetime' (grados Celsius)",
    )
    air_dew_point: Optional[float] = Field(
        None,
        description="Temperatura del punto de rocío calculado correspondiente a "
        "la fecha 'datetime' (grados Celsius)",
    )
    air_humidity: Optional[float] = Field(
        None,
        description="Humedad relativa instantánea del aire correspondiente a la "
        "fecha dada por 'datetime' (%)",
    )

    # wind
    wind_speed_max: Optional[float] = Field(
        None,
        description="Velocidad máxima del viento, valor máximo del viento "
        "mantenido 3 segundos y registrado en los 60 minutos "
        "anteriores a la hora indicada por el período de observación "
        "'datetime' (m/s)",
    )
    wind_speed_average: Optional[float] = Field(
        None,
        description="Velocidad media del viento, media escalar de las muestras "
        "adquiridas cada 0,25 ó 1 segundo en el período de 10 minutos "
        "anterior al indicado por 'datetime' (m/s)",
    )
    wind_speed_deviation: Optional[float] = Field(
        None,
        description="Desviación estándar de las muestras adquiridas de velocidad "
        "del viento durante los 10 minutos anteriores a la fecha dada "
        "por 'datetime' (m/s)",
    )
    wind_direction: Optional[float] = Field(
        None,
        description="Dirección media del viento, en el período de 10 minutos "
        "anteriores a la fecha indicada por 'datetime' (grados)",
    )
    wind_direction_max: Optional[float] = Field(
        None,
        description="Dirección del viento máximo registrado en los 60 minutos "
        "anteriores a la hora indicada por 'datetime' (grados)",
    )
    wind_direction_deviation: Optional[float] = Field(
        None,
        description="Desviación estándar de las muestras adquiridas de la "
        "dirección del viento durante los 10 minutos anteriores a la "
        "fecha dada por 'datetime' (grados)",
    )
    wind_distance: Optional[float] = Field(
        None,
        description="Recorrido del viento durante los 60 minutos anteriores a la "
        "fecha indicada por 'datetime' (Hm)",
    )
    # wind by ultrasonic sensor
    wind_speed_max_ultrasonic: Optional[float] = Field(
        None,
        description="Velocidad máxima del viento (sensor ultrasónico), media "
        "escalar en el periódo de 10 minutos anterior al indicado por "
        "'datetime' de las muestras adquiridas cada 0,25 ó 1 segundo "
        "(m/s)",
    )
    wind_speed_average_ultrasonic: Optional[float] = Field(
        None,
        description="Velocidad máxima del viento (sensor ultrasónico), valor "
        "máximo del viento mantenido 3 segundos y registrado en los "
        "60 minutos anteriores a la hora indicada por el período de "
        "observación 'datetime' (m/s)",
    )

    wind_speed_deviation_ultrasonic: Optional[float] = Field(
        None,
        description="Desviación estándar de las muestras adquiridas de velocidad "
        "del viento durante los 10 minutos anteriores a la fecha dada "
        "por 'datetime' obtenido del sensor ultrasónico de viento "
        "instalado junto al convencional (m/s)",
    )
    wind_direction_ultrasonic: Optional[float] = Field(
        None,
        description="Dirección media del viento (sensor ultrasónico), en el "
        "período de 10 minutos anteriores a la fecha indicada por "
        "'datetime' (grados)",
    )
    wind_direction_max_ultrasonic: Optional[float] = Field(
        None,
        description="Dirección del viento máximo registrado en los 60 minutos "
        "anteriores a la hora indicada por 'datetime' por el sensor "
        "ultrasónico (grados)",
    )
    wind_direction_deviation_ultrasonic: Optional[float] = Field(
        None,
        description="Desviación estándar de las muestras adquiridas de la "
        "dirección del viento durante los 10 minutos anteriores a la "
        "fecha dada por 'datetime' obtenido del sensor ultrasónico de "
        "viento instalado junto al convencional (grados)",
    )

    # pressure
    pressure: Optional[float] = Field(
        None,
        description="Presión instantánea al nivel en el que se encuentra "
        "instalado el barómetro y correspondiente a la fecha dada por "
        "'datetime' (hPa)",
    )
    pressure_sea: Optional[float] = Field(
        None,
        description="Valor de la presión reducido al nivel del mar para aquellas "
        "estaciones cuya altitud es igual o menor a 750 metros y "
        "correspondiente a la fecha indicada por 'datetime' (hPa)",
    )

    # ground
    ground_temperature: Optional[float] = Field(
        None,
        description="Temperatura suelo, temperatura instantánea junto al suelo y "
        "correspondiente a los 10 minutos anteriores a la fecha dada "
        "por 'datetime' (grados Celsius)",
    )
    ground_temperature_5: Optional[float] = Field(
        None,
        description="Temperatura subsuelo 5 cm, temperatura del subsuelo a una "
        "profundidad de 5 cm y correspondiente a los 10 minutos "
        "anteriores a la fecha dada por 'datetime' (grados Celsius)",
    )
    ground_temperature_20: Optional[float] = Field(
        None,
        description="Temperatura subsuelo 20 cm, temperatura del subsuelo a una "
        "profundidad de 20 cm y correspondiente a los 10 minutos "
        "anteriores a la fecha dada por 'datetime' (grados Celsius)",
    )

    # snow
    snow: Optional[float] = Field(
        None,
        description="Espesor de la capa de nieve medida en los 10 minutos "
        "anteriores a la a la fecha indicada por 'datetime' (cm)",
    )

    # visibility
    visibility: Optional[float] = Field(
        None,
        description="Visibilidad, promedio de la medida de la visibilidad "
        "correspondiente a los 10 minutos anteriores a la fecha dada "
        "por 'datetime' (Km)",
    )
    # radiation
    insolation: Optional[float] = Field(
        None,
        description="Duración de la insolación durante los 60 minutos anteriores "
        "a la hora indicada por el período de observación 'datetime' "
        "(horas)",
    )


# Warning Area Data Model
class WarningArea(BaseModel):
    id: str
    area_name: str

    # TODO: transform polygon to geojson
    # polygon: str
    # area_code: Optional[str]


# Warning Data Model
class WarningData(WarningArea):
    """
    # TODO: review real meaning / utility of this data
    """

    # level
    level: str = Field(
        description="Nivel de la aterta",
        examples=["verde", "amarilla", "naranja"],
    )
    # event
    event: str = Field(
        description="Tipo de fenómeno o evento asociado a la alerta",
        examples=["máximas"],
    )
    # zone
    zone: str = Field(
        description="Código de la zona asociada a la aterta",
        examples=["611101"],
    )

    source: str
    sent: Datetime
    status: str
    event_type: str
    audience: str
    language: str
    category: str
    event_code: str
    event_text: str
    urgency: str
    severity: str
    certainty: str
    effective: Datetime
    onset: Datetime
    expires: Datetime
    # headline: str
    # web: str
    # contact: str
    # level: str
    # areas: List[WarningArea]

