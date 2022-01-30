import lnetatmo
import time
from typing import Generator, Tuple

from core.ProjectAliceExceptions import SkillStartingFailed
from core.base.model.AliceSkill import AliceSkill
from core.util.model.TelemetryType import TelemetryType


class Netatmo(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Get readings from your netatmo hardware
	"""

	def __init__(self):
		super().__init__()

		self._netatmoAuth 	= None
		self._weatherData 	= None
		self._authTries 	= 0
		self._telemetryTypes = {
			'Temperature': TelemetryType.TEMPERATURE,
			'CO2': TelemetryType.CO2,
			'Humidity': TelemetryType.HUMIDITY,
			'Noise': TelemetryType.NOISE,
			'Pressure': TelemetryType.PRESSURE,
			'Rain': TelemetryType.RAIN,
			'sum_rain_1': TelemetryType.SUM_RAIN_1,
			'sum_rain_24': TelemetryType.SUM_RAIN_24,
			'WindStrength': TelemetryType.WIND_STRENGTH,
			'WindAngle': TelemetryType.WIND_ANGLE,
			'GustStrength': TelemetryType.GUST_STRENGTH,
			'GustAngle': TelemetryType.GUST_ANGLE
		}


	def onStart(self):
		super().onStart()
		if not self.getConfig('password'):
			raise SkillStartingFailed(skillName=self.name, error='No credentials provided')

		if not self._auth():
			raise SkillStartingFailed(skillName=self.name, error='Authentication failed')

		try:
			self._weatherData = lnetatmo.WeatherStationData(self._netatmoAuth)
		except lnetatmo.NoDevice:
			raise SkillStartingFailed(skillName=self.name, error='No Netatmo device found')


	def _auth(self) -> bool:
		try:
			self._netatmoAuth = lnetatmo.ClientAuth(
				clientId=self.getConfig('clientId'),
				clientSecret=self.getConfig('clientSecret'),
				username=self.getConfig('username'),
				password=self.getConfig('password'),
				scope='read_station'
			)
		except Exception:
			self._authTries += 1
			if self._authTries >= 3:
				raise SkillStartingFailed(skillName=self.name, error='Tried to auth 3 times, giving up now')
			else:
				time.sleep(1)
				return self._auth()

		return True


	def _lastWeatherData(self) -> Generator[Tuple[str, TelemetryType, str], None, None]:
		self._weatherData = lnetatmo.WeatherStationData(self._netatmoAuth)
		for locationName, values in self._weatherData.lastData().items():
			if locationName == 'Wind' or locationName == 'Rain':
				locationName = self.LanguageManager.getStrings('outside')[0]

			for key, value in values.items():
				yield locationName.lower(), self._telemetryTypes.get(key), value


	def onFullMinute(self):
		now = time.time()
		for locationName, ttype, value in self._lastWeatherData():
			if ttype:
				location = self.LocationManager.getLocation(locationName=locationName)
				if location:
					self.TelemetryManager.storeData(ttype=ttype, value=value, deviceId=12345, service=self.name, locationId=location.id, timestamp=now)
				else:
					self.logInfo(f'Got telemetry data for not existing location named "{locationName}"')
