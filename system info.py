import sys
import psutil

print(f"Your platform or OS is {sys.platform}")

print(f"Your PC RAM is {psutil.virtual_memory().total / 1e+9:.2f} GB")
print(f"Your PC CPU is {psutil.cpu_count()} cores")
print(f"Your PC CPU frequency is {psutil.cpu_freq().current:.2f} MHz")
print(f"Your PC CPU usage is {psutil.cpu_percent(interval=1)} %")

disk_usage = psutil.disk_usage('/')
print(f"Your PC disk usage is {disk_usage.percent} %")
print(f"Your PC disk total is {disk_usage.total / 1e+9:.2f} GB")
print(f"Your PC disk used is {disk_usage.used / 1e+9:.2f} GB")
print(f"Your PC disk free is {disk_usage.free / 1e+9:.2f} GB")

disk_io = psutil.disk_io_counters()
print(f"Your PC disk read count is {disk_io.read_count}")
print(f"Your PC disk write count is {disk_io.write_count}")
print(f"Your PC disk read bytes is {disk_io.read_bytes / 1e+9:.2f} GB")
print(f"Your PC disk write bytes is {disk_io.write_bytes / 1e+9:.2f} GB")
print(f"Your PC disk read time is {disk_io.read_time} ms")
print(f"Your PC disk write time is {disk_io.write_time} ms")