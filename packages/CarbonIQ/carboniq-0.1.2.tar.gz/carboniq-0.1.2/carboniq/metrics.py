import time
import psutil
import requests

class CarbonCalculator:
    # Static data for emission factors (kg CO₂/kWh)
    EMISSION_FACTORS = {
        "global": 0.475,
        "us": 0.401,
        "eu": 0.252,
        "asia": 0.634,
        "india": 0.708,
        "china": 0.707,
        "canada": 0.150,
        "australia": 0.783,
        "africa": 0.657,
        "south_america": 0.200
    }

    def __init__(self, region="global"):
        self.region = region.lower()
        self.carbon_factor = self._load_emission_factors()

    def _load_emission_factors(self):
        # Fetch emission factor for the specified region, defaulting to 'global'
        return self.EMISSION_FACTORS.get(self.region, self.EMISSION_FACTORS["global"])

    def fetch_live_emission_factor(self):
        # Fetch live grid intensity using electricityMap API
        try:
            response = requests.get(f"https://api.electricitymap.org/v3/intensity/{self.region}")
            data = response.json()
            return data.get("carbonIntensity", self.carbon_factor)
        except Exception:
            return self.carbon_factor  # Fallback to static data if API fails

    def calculate_emissions(self, energy_kwh):
        # Calculate emissions in kg CO₂
        return energy_kwh * self.carbon_factor

    def estimate_energy(self, cpu_time, memory_usage_mb):
        # Estimate energy consumption in kWh
        cpu_energy = cpu_time * 0.0002
        memory_energy = memory_usage_mb * 0.0001
        return cpu_energy + memory_energy
