import platform
import psutil
import time

def os_name(self = None):
    return platform.system()

def memory_procent(self = None):
    memory_info = psutil.virtual_memory()
    return round(memory_info.percent)

def cpu_procent(self = None):
    return round(psutil.cpu_percent(interval=3))