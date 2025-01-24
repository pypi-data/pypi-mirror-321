import asyncio
import time
from functools import wraps
from inspect import getfile

import psutil
from pynvml import nvmlDeviceGetHandleByIndex, nvmlDeviceGetUtilizationRates, nvmlDeviceGetMemoryInfo

from carboniq.gpu_utils import GPU_ENABLED
from carboniq.metrics import CarbonCalculator

calculator = CarbonCalculator(region="global")

BADGES = [
    {"name": "🌱 Carbon Saver", "range": (0.00, 0.01), "description": "Outstanding eco-efficiency!"},
    {"name": "🌍 Eco-Friendly Coder", "range": (0.01, 0.1), "description": "Good environmental performance."},
    {"name": "🛠️ Code Efficiently Next Time", "range": (0.1, float("inf")), "description": "Optimization needed."},
]

def carbon_profiler(real_time=False):
    """
    Decorator to profile energy usage and carbon emissions of a function.

    Args:
        real_time (bool): Whether to fetch real-time carbon intensity data.

    Returns:
        Callable: A decorated function that logs its carbon profile.
    """
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            return await _execute_and_profile(func, args, kwargs, is_async=True, real_time=real_time)

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            return asyncio.run(_execute_and_profile(func, args, kwargs, is_async=False, real_time=real_time))

        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper

    return decorator

async def _execute_and_profile(func, args, kwargs, is_async, real_time):
    """
    Core logic to profile energy usage and emissions.

    Args:
        func (Callable): The function to execute and profile.
        args (tuple): Positional arguments for the function.
        kwargs (dict): Keyword arguments for the function.
        is_async (bool): Whether the function is asynchronous.
        real_time (bool): Whether to fetch real-time carbon intensity data.

    Returns:
        Any: The result of the executed function.
    """
    # Initial readings
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss / (1024 * 1024)  # MB
    disk_before = process.io_counters().read_bytes + process.io_counters().write_bytes
    net_before = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    # GPU initialization
    gpu_before = gpu_usage_before = 0
    handle = None
    if GPU_ENABLED:
        handle = nvmlDeviceGetHandleByIndex(0)
        gpu_before = nvmlDeviceGetMemoryInfo(handle).used / (1024 * 1024)  # MB
        gpu_usage_before = nvmlDeviceGetUtilizationRates(handle).gpu  # %

    # Execute the function
    result = await func(*args, **kwargs) if is_async else func(*args, **kwargs)

    # Post-execution readings
    end_time = time.time()
    memory_after = process.memory_info().rss / (1024 * 1024)  # MB
    disk_after = process.io_counters().read_bytes + process.io_counters().write_bytes
    net_after = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    cpu_time = end_time - start_time
    memory_used = max(0, memory_after - memory_before)
    disk_usage = max(0, disk_after - disk_before)
    net_usage = max(0, net_after - net_before)

    # GPU readings
    gpu_after = gpu_usage_after = 0
    if GPU_ENABLED:
        gpu_after = nvmlDeviceGetMemoryInfo(handle).used / (1024 * 1024)
        gpu_usage_after = nvmlDeviceGetUtilizationRates(handle).gpu  # %

    # Energy calculations
    disk_energy_kwh = disk_usage * 0.000000001
    net_energy_kwh = net_usage * 0.0000000005
    gpu_memory_used = max(0, gpu_after - gpu_before)
    gpu_utilization = max(0, gpu_usage_after - gpu_usage_before)
    gpu_energy_kwh = gpu_utilization * 0.0003
    energy_kwh = calculator.estimate_energy(cpu_time, memory_used) + disk_energy_kwh + net_energy_kwh + gpu_energy_kwh

    emissions = calculator.calculate_emissions(energy_kwh)

    # Real-time updates
    live_emissions = emissions
    if real_time:
        live_factor = calculator.fetch_live_emission_factor()
        live_emissions = energy_kwh * live_factor

    # File and line information
    file_path = getfile(func)
    line_number = func.__code__.co_firstlineno

    # Determine badge earned
    badge = next(
        (badge_info for badge_info in BADGES if badge_info["range"][0] <= emissions < badge_info["range"][1]), None
    )

    # Print detailed summary
    print("\n=== CarbonIQ Emission Summary ===")
    print(f"File Path: {file_path}")
    print(f"Line Number: {line_number}")
    print(f"Function Name: {func.__name__}")
    print(f"Execution Time: {cpu_time:.6f} seconds")
    print(f"CPU Energy: {calculator.estimate_energy(cpu_time, 0):.6f} kWh")
    print(f"Memory Used: {memory_used:.6f} MB")
    print(f"Disk I/O: {disk_usage / (1024 * 1024):.6f} MB")
    print(f"Network I/O: {net_usage / (1024 * 1024):.6f} MB")
    print(f"GPU Utilization: {gpu_utilization:.6f} %")
    print(f"GPU Memory Used: {gpu_memory_used:.6f} MB")
    print(f"Total Energy Consumed: {energy_kwh:.6f} kWh")
    print(f"Estimated Emissions: {emissions:.6f} kg CO2")
    if real_time:
        print(f"Real-Time Emissions: {live_emissions:.6f} kg CO2")
    if badge:
        print(f"Badge Earned: {badge['name']} ({badge['description']})")
    print("\n=== Badge Ranges ===")
    for badge_info in BADGES:
        print(f"{badge_info['name']}: {badge_info['range'][0]} - {badge_info['range'][1]} kg CO2 ({badge_info['description']})")
    print("=================================\n")

    return result
