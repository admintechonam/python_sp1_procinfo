import typer
from common_utils.procinfo_utils import get_top_process, get_proc_details, display_proc_info, display_procs, diplay_menu

app = typer.Typer()

@app.command()
def main(platform: str = typer.Option(None, help="Platform name (must be 'windows')"), top_count: int = 5):
    if not platform:
        print("Error: --platform is a mandatory argument. Please provide it (e.g., --platform windows).")
        raise SystemExit("Exiting...")
    if platform.lower() != 'windows':
        print("This script is only for Windows platform")
        raise SystemExit("Exiting...")
    diplay_menu(top_count)

if __name__ == "__main__":
    app()
