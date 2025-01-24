import json
import time
import psutil
import requests
import os
from pathlib import Path

class CarbonCalculator:
    def __init__(self, region="global"):
        self.region = region
        self.project_root = Path(__file__).resolve().parent  # Dynamically determine the root folder
        self.carbon_factor = self._load_emission_factors()

    def _load_emission_factors(self):
        # Construct the dynamic path to the emission factors file
        data_file = self.project_root / "data/emission_factors.json"
        try:
            with open(data_file, "r") as f:
                emission_factors = json.load(f)
            return emission_factors.get(self.region.lower(), 0.475)
        except FileNotFoundError:
            raise FileNotFoundError(f"Emission factors file not found at: {data_file}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in: {data_file}")

    def fetch_live_emission_factor(self):
        # Fetch live grid intensity using electricityMap API
        try:
            response = requests.get(f"https://api.electricitymap.org/v3/intensity/{self.region}")
            data = response.json()
            return data.get("carbonIntensity", self.carbon_factor)
        except Exception:
            return self.carbon_factor  # Fallback to default if API fails

    def calculate_emissions(self, energy_kwh):
        return energy_kwh * self.carbon_factor

    def estimate_energy(self, cpu_time, memory_usage_mb):
        # Energy estimation based on device calibration
        cpu_energy = cpu_time * 0.0002
        memory_energy = memory_usage_mb * 0.0001
        return cpu_energy + memory_energy
