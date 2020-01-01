# Netatmo

### Download

##### > WGET method
```bash
wget http://skills.projectalice.ch/Netatmo -O ~/ProjectAlice/system/skillInstallTickets/Netatmo.install
```

### Description
Get readings from your netatmo hardware

- Version: 1.0.8
- Author: Psychokiller1888
- Maintainers: maxbachmann
- Alice minimum Version: 1.0.0-a4
- Conditions:
  - en
  - fr
  - de
  - online
  - TelemetryManager activated
- Pip requirements: N/A
- System requirements: N/A

### Configuration


`clientId`:
 - type: `str`
 - desc: `Your Netatmo dev account client id`

`clientSecret`:
 - type: `str`
 - desc: `Your Netatmo dev account client secret key`

`username`:
 - type: `str`
 - desc: `Your Netatmo account username`

`password`:
 - type: `str`
 - desc: `Your Netatmo account password`

`WindAlertFromKmh`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`TemperatureAlertHigh`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`TemperatureAlertLow`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`CO2AlertHigh`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`HumidityAlertHigh`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`HumidityAlertLow`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`PressureAlertHigh`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`

`PressureAlertLow`:
 - type: `int`
 - desc: `An event is broadcasted when this limit is reached`
