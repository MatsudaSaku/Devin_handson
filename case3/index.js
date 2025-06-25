#!/usr/bin/env node

import { Command } from 'commander';
import axios from 'axios';
import chalk from 'chalk';
import dotenv from 'dotenv';

dotenv.config();

const program = new Command();

program
  .name('weather-cli')
  .description('CLI tool to fetch weather information')
  .version('1.0.0')
  .argument('<city>', 'city name to get weather for')
  .option('-u, --units <type>', 'temperature units (metric, imperial, kelvin)', 'metric')
  .action(async (city, options) => {
    try {
      await getWeather(city, options.units);
    } catch (error) {
      console.error(chalk.red('Error:'), error.message);
      process.exit(1);
    }
  });

async function getWeather(city, units = 'metric') {
  const apiKey = process.env.WEATHER_API_KEY;
  const baseUrl = process.env.WEATHER_API_BASE_URL || 'https://api.openweathermap.org/data/2.5';
  
  if (!apiKey) {
    throw new Error('WEATHER_API_KEY environment variable is required. Please check your .env file.');
  }

  console.log(chalk.blue(`🌤️  Fetching weather for ${chalk.bold(city)}...`));
  
  try {
    const response = await axios.get(`${baseUrl}/weather`, {
      params: {
        q: city,
        appid: apiKey,
        units: units
      }
    });

    const weatherData = response.data;
    displayWeather(weatherData, units);
    
  } catch (error) {
    if (error.response?.status === 404) {
      throw new Error(`City "${city}" not found. Please check the spelling and try again.`);
    } else if (error.response?.status === 401) {
      throw new Error('Invalid API key. Please check your WEATHER_API_KEY in .env file.');
    } else {
      throw new Error(`Failed to fetch weather data: ${error.message}`);
    }
  }
}

function displayWeather(data, units) {
  const unitSymbol = units === 'metric' ? '°C' : units === 'imperial' ? '°F' : 'K';
  
  console.log('\n' + chalk.green('='.repeat(50)));
  console.log(chalk.green.bold(`Weather Information for ${data.name}, ${data.sys.country}`));
  console.log(chalk.green('='.repeat(50)));
  
  const coloredData = {
    location: {
      city: chalk.cyan(data.name),
      country: chalk.cyan(data.sys.country),
      coordinates: {
        latitude: chalk.yellow(data.coord.lat),
        longitude: chalk.yellow(data.coord.lon)
      }
    },
    weather: {
      main: chalk.magenta(data.weather[0].main),
      description: chalk.magenta(data.weather[0].description),
      icon: chalk.blue(data.weather[0].icon)
    },
    temperature: {
      current: chalk.red(`${data.main.temp}${unitSymbol}`),
      feels_like: chalk.red(`${data.main.feels_like}${unitSymbol}`),
      min: chalk.blue(`${data.main.temp_min}${unitSymbol}`),
      max: chalk.red(`${data.main.temp_max}${unitSymbol}`)
    },
    atmospheric: {
      pressure: chalk.gray(`${data.main.pressure} hPa`),
      humidity: chalk.cyan(`${data.main.humidity}%`),
      visibility: chalk.gray(`${(data.visibility / 1000).toFixed(1)} km`)
    },
    wind: {
      speed: chalk.green(`${data.wind.speed} ${units === 'metric' ? 'm/s' : 'mph'}`),
      direction: chalk.green(`${data.wind.deg}°`)
    },
    clouds: {
      coverage: chalk.gray(`${data.clouds.all}%`)
    },
    sun: {
      sunrise: chalk.yellow(new Date(data.sys.sunrise * 1000).toLocaleTimeString()),
      sunset: chalk.yellow(new Date(data.sys.sunset * 1000).toLocaleTimeString())
    },
    timestamp: chalk.gray(new Date(data.dt * 1000).toLocaleString())
  };

  console.log(JSON.stringify(coloredData, null, 2));
  console.log(chalk.green('='.repeat(50)) + '\n');
}

program.parse();
