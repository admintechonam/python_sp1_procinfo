import psutil


class ProcIUtils:
    def __init__(self):
        self.top_n_processes = {}

    def get_top_process(self, top_count):
        print(f"Listing the top {top_count} running processes:")
        self.top_n_processes.clear()
        for i, proc in enumerate(psutil.process_iter(['name', 'pid']), start=1):
            if i > top_count:
                break
            self.top_n_processes[i] = {'name': proc.info['name'], 'pid': proc.info['pid']}

    def get_proc_details(self):
        selected_process = int(input("Select a process by number: "))
        proc_info = {
            "name": self.top_n_processes[selected_process]['name'],
            "pid": self.top_n_processes[selected_process]['pid'],
            "memory_MB": psutil.Process(self.top_n_processes[selected_process]['pid']).memory_info().rss / (1024 * 1024),
            "cpu_percent": psutil.Process(self.top_n_processes[selected_process]['pid']).cpu_percent(interval=1),
            "disk_io": psutil.Process(self.top_n_processes[selected_process]['pid']).io_counters()
        }
        return proc_info