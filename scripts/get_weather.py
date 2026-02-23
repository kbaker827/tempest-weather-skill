#!/usr/bin/env python3
"""
Fetch current weather data from a Tempest WeatherFlow station.

Usage:
    python3 get_weather.py --station 207824 --token YOUR_TOKEN
    python3 get_weather.py --station 207824 --token YOUR_TOKEN --format json

Get your API token from the WeatherFlow app:
    Settings → Data → API Token
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime

# Tempest API endpoint
API_URL = "https://swd.weatherflow.com/swd/rest/observations/station/{station_id}"

def get_weather(station_id: str, token: str) -> dict:
    """Fetch weather data for a station."""
    url = API_URL.format(station_id=station_id)
    url += f"?token={token}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Error: Invalid or missing API token.", file=sys.stderr)
            print("Get your token from the WeatherFlow app: Settings → Data → API Token", file=sys.stderr)
        else:
            print(f"Error: HTTP {e.code} - {e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching weather: {e}", file=sys.stderr)
        sys.exit(1)

def format_conditions(data: dict) -> str:
    """Format weather data for display."""
    if 'obs' not in data or not data['obs']:
        return "No observation data available."
    
    obs = data['obs'][0]
    
    lines = [
        f"Station: {data.get('station_name', 'Unknown')}",
        f"Time: {datetime.fromtimestamp(obs.get('timestamp', 0)).strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Temperature: {obs.get('air_temperature', 'N/A')}°F" if 'air_temperature' in obs else "",
        f"Humidity: {obs.get('relative_humidity', 'N/A')}%" if 'relative_humidity' in obs else "",
        f"Pressure: {obs.get('station_pressure', 'N/A')} mb" if 'station_pressure' in obs else "",
        f"Wind: {obs.get('wind_avg', 'N/A')} mph from {obs.get('wind_direction', 'N/A')}°" if 'wind_avg' in obs else "",
        f"Wind Gust: {obs.get('wind_gust', 'N/A')} mph" if 'wind_gust' in obs else "",
        f"Rain Today: {obs.get('precip_accum_local_day', 'N/A')}\"" if 'precip_accum_local_day' in obs else "",
        f"UV Index: {obs.get('uv', 'N/A')}" if 'uv' in obs else "",
        f"Solar Radiation: {obs.get('solar_radiation', 'N/A')} W/m²" if 'solar_radiation' in obs else "",
    ]
    
    return "\n".join(line for line in lines if line)

def main():
    parser = argparse.ArgumentParser(description='Get Tempest weather data')
    parser.add_argument('--station', '-s', required=True, help='Station ID')
    parser.add_argument('--token', '-t', help='API token (or set TEMPEST_API_TOKEN env var)')
    parser.add_argument('--format', '-f', choices=['json', 'text'], default='text',
                       help='Output format')
    
    args = parser.parse_args()
    
    # Get token from args or environment
    token = args.token or os.environ.get('TEMPEST_API_TOKEN')
    if not token:
        print("Error: API token required.", file=sys.stderr)
        print("Usage: python3 get_weather.py --station 207824 --token YOUR_TOKEN", file=sys.stderr)
        print("Or set TEMPEST_API_TOKEN environment variable", file=sys.stderr)
        print("\nGet your token from the WeatherFlow app: Settings → Data → API Token", file=sys.stderr)
        sys.exit(1)
    
    data = get_weather(args.station, token)
    
    if args.format == 'json':
        print(json.dumps(data, indent=2))
    else:
        print(format_conditions(data))

if __name__ == '__main__':
    main()
