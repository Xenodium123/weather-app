from weather_report_factory.py import WeatherReportFactory
from weather_api.py import WeatherAPI

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    weather_api = WeatherAPI(api_key)

    city = input("Podaj nazwę miasta: ")
    format_type = input("Podaj format raportu (np. json): ").lower()

    try:
        weather_data = weather_api.get_weather(city)
        report = WeatherReportFactory.get_report(format_type)
        print(report.generate_report(weather_data))
    except Exception as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()
