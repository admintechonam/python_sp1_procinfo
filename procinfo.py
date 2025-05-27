import typer

from common_utils.procinfo_utils import ProcIUtils
from common_utils.procinfo_display import MenuHandler


app = typer.Typer()
proc_utils = ProcIUtils()
menu = MenuHandler(proc_utils)

@app.command()
def main(platform: str = typer.Option(None, help="Platform name (must be 'windows')"), top_count: int = 5):
    if not platform:
        print("Error: --platform is a mandatory argument. Please provide it (e.g., --platform windows).")
        raise SystemExit("Exiting...")
    if platform.lower() != 'windows':
        print("This script is only for Windows platform")
        raise SystemExit("Exiting...")
    menu.display_menu(top_count)

if __name__ == "__main__":
    app()
