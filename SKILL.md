---
name: tempest-weather
description: Access weather data from Tempest WeatherFlow personal weather stations. Use when the user asks about current weather, temperature, wind, rain, or conditions from their Tempest station, or needs to query the Tempest API for weather data. Requires an API token from WeatherFlow.
---

# Tempest Weather

Access real-time weather data from Tempest WeatherFlow personal weather stations via the REST API.

## Quick Start

### Station Configuration

Get your Station ID from your Tempest dashboard URL:
- URL format: `https://tempestwx.com/station/{STATION_ID}/`
- Example: `https://tempestwx.com/station/12345/`
- Station ID would be: `12345`

### API Token

You need an API token from WeatherFlow:
1. Open the WeatherFlow app
2. Go to Settings → Data → API Token
3. Copy the token

Or set the environment variable: `export TEMPEST_API_TOKEN=your_token_here`

### Get Current Conditions

```bash
# Using the provided script
python3 scripts/get_weather.py --station YOUR_STATION_ID --token YOUR_TOKEN

# Using curl directly
curl -s "https://swd.weatherflow.com/swd/rest/observations/station/YOUR_STATION_ID?token=YOUR_TOKEN" | jq '.obs[0]'
```

### Key API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/swd/rest/observations/station/{id}` | Current observations for station |
| `/swd/rest/observations/device/{id}` | Current observations for device |
| `/swd/rest/stations` | List all stations for token |

### Common Observation Fields

| Field | Description | Units |
|-------|-------------|-------|
| `air_temperature` | Temperature | °F or °C |
| `relative_humidity` | Humidity | % |
| `station_pressure` | Pressure | mb/hPa |
| `wind_avg` | Wind speed | mph or km/h |
| `wind_direction` | Wind direction | degrees |
| `wind_gust` | Wind gust | mph or km/h |
| `precip_accum_local_day` | Daily rainfall | in or mm |
| `uv` | UV index | 0-11+ |
| `solar_radiation` | Solar radiation | W/m² |

## Resources

### scripts/
- `get_weather.py` - Fetch and display current conditions (requires `--token` or `TEMPEST_API_TOKEN` env var)

### references/
- `api-reference.md` - Full Tempest API documentation

## Examples

### Get weather as formatted text
```bash
python3 scripts/get_weather.py --station 12345 --token YOUR_TOKEN
```

### Get weather as JSON
```bash
python3 scripts/get_weather.py --station 12345 --token YOUR_TOKEN --format json
```

### Using environment variable
```bash
export TEMPEST_API_TOKEN=your_token
python3 scripts/get_weather.py --station 12345
```
