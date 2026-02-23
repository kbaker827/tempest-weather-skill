# Tempest Weather Skill for OpenClaw

Access real-time weather data from your Tempest WeatherFlow personal weather station.

## What is OpenClaw?

[OpenClaw](https://github.com/openclaw/openclaw) is an open-source agent framework. This skill extends OpenClaw with Tempest WeatherFlow integration.

## Setup

### 1. Find Your Station ID

Look at your Tempest dashboard URL:
```
https://tempestwx.com/station/12345/
```
Your Station ID is `12345`.

### 2. Get Your API Token

1. Open the WeatherFlow app
2. Go to **Settings → Data → API Token**
3. Copy your token

### 3. Use the Skill

```bash
# Get current weather
python3 scripts/get_weather.py --station 12345 --token YOUR_TOKEN

# Get JSON output
python3 scripts/get_weather.py --station 12345 --token YOUR_TOKEN --format json

# Or use environment variable
export TEMPEST_API_TOKEN=your_token
python3 scripts/get_weather.py --station 12345
```

## Features

- Current temperature, humidity, pressure
- Wind speed and direction
- Daily rainfall accumulation
- UV index and solar radiation
- JSON or formatted text output

## API Reference

See [`references/api-reference.md`](references/api-reference.md) for complete Tempest API documentation.

## License

MIT
