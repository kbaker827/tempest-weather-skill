# Tempest WeatherFlow API Reference

## Authentication

The Tempest API uses token-based authentication. You can use:
- **Personal Access Token**: Get from the WeatherFlow app → Settings → Data → API Token
- **Public Stations**: Some data is available without a token

## Base URL

```
https://swd.weatherflow.com/swd/rest
```

## Endpoints

### Get Station Observations

```
GET /observations/station/{station_id}
```

Returns current observations for a station.

**Parameters:**
- `station_id` (path): Station ID

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `station_id` | integer | Station ID |
| `station_name` | string | Station name |
| `public_name` | string | Public station name |
| `latitude` | float | Station latitude |
| `longitude` | float | Station longitude |
| `timezone` | string | Timezone |
| `obs` | array | Observation data array |

**Observation Object:**

| Field | Type | Description | Units |
|-------|------|-------------|-------|
| `timestamp` | integer | Unix timestamp | seconds |
| `air_temperature` | float | Temperature | °F or °C |
| `relative_humidity` | float | Humidity | % |
| `station_pressure` | float | Pressure | mb/hPa |
| `sea_level_pressure` | float | Sea level pressure | mb/hPa |
| `wind_avg` | float | Wind speed | mph or km/h |
| `wind_direction` | integer | Wind direction | degrees (0-360) |
| `wind_gust` | float | Wind gust | mph or km/h |
| `precip` | float | Precipitation rate | in/hr or mm/hr |
| `precip_accum_local_day` | float | Daily rainfall | in or mm |
| `uv` | float | UV index | 0-11+ |
| `solar_radiation` | float | Solar radiation | W/m² |
| `brightness` | integer | Brightness | lux |
| `feels_like` | float | Feels like temperature | °F or °C |
| `dew_point` | float | Dew point | °F or °C |
| `wet_bulb_temperature` | float | Wet bulb temperature | °F or °C |
| `delta_t` | float | Delta T | °F or °C |
| `air_density` | float | Air density | kg/m³ |

### Get Device Observations

```
GET /observations/device/{device_id}
```

Returns observations for a specific device.

### List Stations

```
GET /stations
```

Returns all stations associated with your token.

## Example Response

```json
{
  "station_id": 207824,
  "station_name": "My Weather Station",
  "public_name": "Public Station Name",
  "latitude": 35.0,
  "longitude": -77.0,
  "timezone": "America/New_York",
  "obs": [
    {
      "timestamp": 1708632000,
      "air_temperature": 72.5,
      "relative_humidity": 65,
      "station_pressure": 1013.2,
      "wind_avg": 5.2,
      "wind_direction": 180,
      "wind_gust": 8.1,
      "precip_accum_local_day": 0.05,
      "uv": 3.2,
      "solar_radiation": 450
    }
  ]
}
```

## Rate Limits

- Public endpoints: 100 requests per minute
- Authenticated endpoints: Higher limits apply

## Official Documentation

Full API documentation: https://weatherflow.github.io/Tempest/
