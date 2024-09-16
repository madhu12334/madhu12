import psutil

cpu_threshold = 80
mem_threshold = 80
disk_threshold = 80

cpu_usage = psutil.cpu_percent(interval=1)
mem_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

if cpu_usage > cpu_threshold:
    print("CPU usage is high:", cpu_usage)
if mem_usage > mem_threshold:
    print("Memory usage is high:", mem_usage)
if disk_usage > disk_threshold:
    print("Disk usage is high:", disk_usage)

for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    if proc.info['cpu_percent'] > 80:
        print(f"High CPU process: {proc.info['name']} (PID: {proc.info['pid']})")
