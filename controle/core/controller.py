from datetime import datetime, date
from typing import Literal, Union, Optional

from dateparser import parse


CARIMBO = Literal['dd/mm/YYYY HH:MM:SS', 'dd-mm-YYYY HH:MM:SS']

class ControllerHour:

    def __init__(self, carimbo: CARIMBO):
        pass
    