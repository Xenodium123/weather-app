
from abc import ABC, abstractmethod

class WeatherReport(ABC):
    @abstractmethod
    def generate_report(self, weather_data):
        pass

class JSONWeatherReport(WeatherReport):
    def generate_report(self, weather_data):
        import json
        return json.dumps(weather_data, indent=4)

class WeatherReportFactory:
    @staticmethod
    def get_report(format_type):
        if format_type == "json":
            return JSONWeatherReport()
        # Można tu dodać inne formaty raportów w przyszłości.
        else:
            raise ValueError(f"Nieobsługiwany format raportu: {format_type}")
