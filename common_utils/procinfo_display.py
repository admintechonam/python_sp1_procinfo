class MenuHandler:
    def __init__(self, proc_utils):
        self.proc_utils = proc_utils

    def display_menu(self, top_count):
        self.proc_utils.get_top_process(top_count)
        self.display_procs()
        while True:
            proc_info = self.proc_utils.get_proc_details()
            self.display_proc_info(proc_info)
            cont = input("Do you want to continue? (y/n): ").strip().lower()
            if cont == 'y':
                continue
            elif cont == 'n':
                print("Exiting...")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def display_procs(self):
        for key, value in self.proc_utils.top_n_processes.items():
            print(f"{key}: {value['name']}")

    def display_proc_info(self, proc_info):
        if proc_info:
            print(f"Memory consumption: {proc_info['memory_MB']} MB \n")
            print(f"CPU Utilization: {proc_info['cpu_percent']}% \n")
            print(f"Disk Utilization : {proc_info['disk_io']} \n")