import subprocess
from pathlib import Path

gui_path = Path(__file__).parents[2].joinpath('controle', 'gui', 'app.py')

def main():
    subprocess.run(['python', gui_path.as_posix()])

if __name__ == "__main__":
    main()
