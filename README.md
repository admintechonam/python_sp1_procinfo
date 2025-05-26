# ProcInfo

A Python CLI tool to display process information (memory, CPU, disk usage) for Windows using Typer and psutil.

## Features
- List top N running processes
- Show memory, CPU, and disk usage for a selected process
- User-friendly CLI with prompts

## Requirements
- Python 3.11+
- Windows OS
- [psutil](https://pypi.org/project/psutil/)
- [typer](https://pypi.org/project/typer/)

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python procinfo.py --platform windows --top-count 5
```

## Project Structure
- `procinfo.py`: Main CLI application
- `requirements.txt`: Python dependencies

## License
MIT
