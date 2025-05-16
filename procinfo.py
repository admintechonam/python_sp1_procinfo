import psutil
import typer
# modules : deafult 
# third-party 

# basic understanding of stack & queue : os concepts 

app=typer.Typer()


def get_top_process(count):
    pass

def get_proc_details(proc_name):
    """
    return  : dict  contains {"cpu": x,  "memory": y, "DU": z}
    """
    pass

def display_proc_info(dict):
    pass

def display_procs():
    pass

def diplay_menu():
    # showinng process on the console 
    get_top_process()
    display_procs()
    # while loop logic 
    get_proc_details()
    display_proc_info

@app.command()             
def main(platform: str = '', top_count: int = 5):
     # Input validation : platform is mandatory arg
     # top_count is deafult arg 
    if platform.lower() != 'windows':
        print("This script is only for Windows platform")
        return
        # instaed of return exit the program :  

    diplay_menu()




if __name__ == "__main__":
    app()













