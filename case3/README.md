# 天気情報CLI

OpenWeatherMap APIを使用してカラフルな天気情報を表示するコマンドラインインターフェースです。

## セットアップ

1. 依存関係をインストール:
   ```bash
   npm install
   ```

2. [OpenWeatherMap](https://openweathermap.org/api)から無料のAPIキーを取得

3. `.env.example`を基に`.env`ファイルを作成:
   ```bash
   cp .env.example .env
   ```

4. `.env`ファイルにAPIキーを追加:
   ```
   WEATHER_API_KEY=あなたの実際のAPIキー
   ```

## 使用方法

```bash
# 基本的な使用方法
node index.js Tokyo

# 温度単位を指定
node index.js Tokyo --units imperial
node index.js Tokyo --units metric
node index.js Tokyo --units kelvin

# ヘルプ表示
node index.js --help
```

## 機能

- 🌈 カラフルなJSON出力
- 🌡️ 複数の温度単位対応（摂氏、華氏、ケルビン）
- 🌍 世界中の都市に対応
- ⚡ 高速なAPI応答
- 🔒 環境変数による安全なAPIキー管理

## 出力例

CLIは以下の情報をカラフルで構造化されたJSON形式で表示します：
- 位置情報（都市、国、座標）
- 現在の天気状況
- 気温情報（現在、体感、最低/最高）
- 大気データ（気圧、湿度、視界）
- 風の情報
- 雲の覆い
- 日の出/日の入り時刻
