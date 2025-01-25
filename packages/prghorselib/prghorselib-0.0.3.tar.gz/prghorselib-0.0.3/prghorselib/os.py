import platform
import psutil
import time

def os_name():
    return platform.system()

def memory_procent():
    memory_info = psutil.virtual_memory()
    return round(memory_info.percent)

def cpu_procent():
    return round(psutil.cpu_percent(interval=3))