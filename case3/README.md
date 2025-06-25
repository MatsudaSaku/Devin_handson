# Weather CLI

A colorful command-line interface for fetching weather information using the OpenWeatherMap API.

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

3. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Add your API key to the `.env` file:
   ```
   WEATHER_API_KEY=your_actual_api_key_here
   ```

## Usage

```bash
# Basic usage
node index.js Tokyo

# With temperature units
node index.js Tokyo --units imperial
node index.js Tokyo --units metric
node index.js Tokyo --units kelvin

# Help
node index.js --help
```

## Features

- 🌈 Colorful JSON output
- 🌡️ Multiple temperature units (Celsius, Fahrenheit, Kelvin)
- 🌍 Works with any city worldwide
- ⚡ Fast API responses
- 🔒 Secure API key management with environment variables

## Example Output

The CLI displays weather information in a colorful, structured JSON format including:
- Location details (city, country, coordinates)
- Current weather conditions
- Temperature information (current, feels like, min/max)
- Atmospheric data (pressure, humidity, visibility)
- Wind information
- Cloud coverage
- Sunrise/sunset times
