from pynvml import nvmlInit, nvmlShutdown

try:
    nvmlInit()  # Initialize the NVML library
    GPU_ENABLED = True
    print("[CarbonIQ] NVML successfully initialized. GPU tracking is enabled.")
except ImportError:
    GPU_ENABLED = False
    print("[CarbonIQ] Warning: pynvml not installed. GPU usage will not be tracked.")
except Exception as e:
    GPU_ENABLED = False
    print(f"[CarbonIQ] Warning: NVML initialization failed. Reason: {str(e)}")

def shutdown_nvml():
    """Shutdown the NVML library."""
    if GPU_ENABLED:
        nvmlShutdown()
        print("[CarbonIQ] NVML successfully shutdown.")
