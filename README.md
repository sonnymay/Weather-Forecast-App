# Weather-Forecast-App

This is a simple Weather Forecast App built with Python. It uses the OpenWeatherMap API to fetch weather details of a city.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install:

- Python 3.8 or higher
- tkinter
- requests
- python-dotenv

You can install the necessary libraries by using the following command:

```bash
pip install tk requests python-dotenv
```

### Installation

1. Clone this repository:

```bash
git clone https://github.com/sonnymay/WeatherForecastApp.git
```

2. Navigate to the project directory:

```bash
cd WeatherForecastApp
```

3. Create a `.env` file in the root directory of the project and update your OpenWeatherMap API Key:

```env
OPEN_WEATHER_MAP_API_KEY=your_api_key
```
Please replace `"your_api_key"` with your actual API Key.

4. Run the Python script:

```bash
python main.py
```

## How to use?

Enter a city name in the text field and press 'Get Weather' button. It will display the weather information for that city.

## Authors

- **sonnymay**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenWeatherMap API for providing weather data.
