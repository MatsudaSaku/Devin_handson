#!/usr/bin/env node

import { Command } from 'commander';
import axios from 'axios';
import chalk from 'chalk';
import dotenv from 'dotenv';

dotenv.config();

const program = new Command();

program
  .name('weather-cli')
  .description('天気情報を取得するCLIツール')
  .version('1.0.0')
  .argument('<city>', '天気を取得する都市名')
  .option('-u, --units <type>', '温度単位 (metric, imperial, kelvin)', 'metric')
  .action(async (city, options) => {
    try {
      await getWeather(city, options.units);
    } catch (error) {
      console.error(chalk.red('エラー:'), error.message);
      process.exit(1);
    }
  });

async function getWeather(city, units = 'metric') {
  const apiKey = process.env.WEATHER_API_KEY;
  const baseUrl = process.env.WEATHER_API_BASE_URL || 'https://api.openweathermap.org/data/2.5';
  
  if (!apiKey) {
    throw new Error('WEATHER_API_KEY環境変数が必要です。.envファイルを確認してください。');
  }

  console.log(chalk.blue(`🌤️  ${chalk.bold(city)}の天気情報を取得中...`));
  
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
      throw new Error(`都市「${city}」が見つかりません。スペルを確認して再試行してください。`);
    } else if (error.response?.status === 401) {
      throw new Error('無効なAPIキーです。.envファイルのWEATHER_API_KEYを確認してください。');
    } else {
      throw new Error(`天気データの取得に失敗しました: ${error.message}`);
    }
  }
}

function displayWeather(data, units) {
  const unitSymbol = units === 'metric' ? '°C' : units === 'imperial' ? '°F' : 'K';
  
  console.log('\n' + chalk.green('='.repeat(50)));
  console.log(chalk.green.bold(`${data.name}, ${data.sys.country}の天気情報`));
  console.log(chalk.green('='.repeat(50)));
  
  const coloredData = {
    位置情報: {
      都市: chalk.cyan(data.name),
      国: chalk.cyan(data.sys.country),
      座標: {
        緯度: chalk.yellow(data.coord.lat),
        経度: chalk.yellow(data.coord.lon)
      }
    },
    天気: {
      概況: chalk.magenta(data.weather[0].main),
      詳細: chalk.magenta(data.weather[0].description),
      アイコン: chalk.blue(data.weather[0].icon)
    },
    気温: {
      現在: chalk.red(`${data.main.temp}${unitSymbol}`),
      体感: chalk.red(`${data.main.feels_like}${unitSymbol}`),
      最低: chalk.blue(`${data.main.temp_min}${unitSymbol}`),
      最高: chalk.red(`${data.main.temp_max}${unitSymbol}`)
    },
    大気: {
      気圧: chalk.gray(`${data.main.pressure} hPa`),
      湿度: chalk.cyan(`${data.main.humidity}%`),
      視界: chalk.gray(`${(data.visibility / 1000).toFixed(1)} km`)
    },
    風: {
      風速: chalk.green(`${data.wind.speed} ${units === 'metric' ? 'm/s' : 'mph'}`),
      風向: chalk.green(`${data.wind.deg}°`)
    },
    雲: {
      雲量: chalk.gray(`${data.clouds.all}%`)
    },
    太陽: {
      日の出: chalk.yellow(new Date(data.sys.sunrise * 1000).toLocaleTimeString('ja-JP')),
      日の入り: chalk.yellow(new Date(data.sys.sunset * 1000).toLocaleTimeString('ja-JP'))
    },
    取得時刻: chalk.gray(new Date(data.dt * 1000).toLocaleString('ja-JP'))
  };

  console.log(JSON.stringify(coloredData, null, 2));
  console.log(chalk.green('='.repeat(50)) + '\n');
}

program.parse();
