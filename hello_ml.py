import platform
import os
import psutil

print(f"Hello, ML World from Jenkins!")

print(f"Python version: {platform.python_version()}")

print(f"Operating System: {platform.system()}  {platform.release()}")

print(f"CPU cores: {os.cpu_count}")

print(f"Total RAM: {round(psutil.virtual_memory().total / (1024 ** 3),2)} GB")

