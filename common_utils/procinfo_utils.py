import psutil

top_n_processes = {}

def get_top_process(top_count):
    print(f"Listing the top {top_count} running processes:")
    for i, proc in enumerate(psutil.process_iter(['name', 'pid']), start=1):
        if i > top_count:
            break
        top_n_processes.update({i: {'name': proc.info['name'], 'pid': proc.info['pid']}})

def get_proc_details():
    selected_process = int(input("Select a process by number: "))
    proc_info = {
        "name": top_n_processes[selected_process]['name'],
        "pid": top_n_processes[selected_process]['pid'],
        "memory_MB": psutil.Process(top_n_processes[selected_process]['pid']).memory_info().rss / (1024 * 1024),
        "cpu_percent": psutil.Process(top_n_processes[selected_process]['pid']).cpu_percent(interval=1),
        "disk_io": psutil.Process(top_n_processes[selected_process]['pid']).io_counters()
    }
    return proc_info

def display_proc_info(proc_info):
    if proc_info:
        print(f"Memory consumption: {proc_info['memory_MB']} MB \n")
        print(f"CPU Utilization: {proc_info['cpu_percent']}% \n")
        print(f"Disk Utilization : {proc_info['disk_io']} \n")

def display_procs():
    for key, value in top_n_processes.items():
        print(f"{key}: {value['name']}")

def diplay_menu(top_count):
    get_top_process(top_count)
    display_procs()
    while True:
        proc_info = get_proc_details()
        display_proc_info(proc_info)
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont == 'y':
            continue
        elif cont == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
