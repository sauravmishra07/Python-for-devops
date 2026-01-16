import psutil

def get_thresholds():
    cpu_threshold = float(input("Enter CPU usage threshold (%): "))
    memory_threshold = float(input("Enter Memory usage threshold (%): "))
    disk_threshold = float(input("Enter Disk usage threshold (%): "))
    return cpu_threshold, memory_threshold, disk_threshold

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, memory_usage, disk_usage

def check_threshold(metric_name, usage, threshold):
    if usage > threshold:
        print(f"⚠️  {metric_name} usage HIGH: {usage}% (Threshold: {threshold}%)")
    else:
        print(f"✅ {metric_name} usage OK: {usage}% (Threshold: {threshold}%)")

def main():
    print("=== System Resource Monitor ===")
    cpu_t, mem_t, disk_t = get_thresholds()

    cpu, memory, disk = get_system_metrics()

    print("\n--- Current System Usage ---")
    check_threshold("CPU", cpu, cpu_t)
    check_threshold("Memory", memory, mem_t)
    check_threshold("Disk", disk, disk_t)

if __name__ == "__main__":
    main()
