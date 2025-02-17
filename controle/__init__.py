from pathlib import Path
from typing import Literal

INSTANCE_PATH: Path = Path(__file__).parents[2].joinpath('instance')
CARIMBO = Literal['dd/mm/YYYY HH:MM:SS', 'dd-mm-YYYY HH:MM:SS', 'dd/mm/YYYY', 'dd-mm-YYYY', 'HH:MM:SS']

if not INSTANCE_PATH.exists():
    INSTANCE_PATH.mkdir(parents=True)