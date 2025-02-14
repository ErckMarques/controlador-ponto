from datetime import datetime, date

from typing import Literal, Union, Optional

from dateparser import parse
from controle.core.exceptions import DataFormatInvalidError, DataInvalidError

CARIMBO = Literal['dd/mm/YYYY HH:MM:SS', 'dd-mm-YYYY HH:MM:SS', 'dd/mm/YYYY', 'dd-mm-YYYY', 'HH:MM:SS']

class _ValidateData:
    """Esta classe é responsável por validar a data.
    """
    
    @classmethod
    def validar(self, valor_data: Union[str, datetime] = None) -> datetime:
        if valor_data is None:
            raise DataInvalidError('Data não informada. Informe uma data E em um formato válido.')
        
        try:
            parsed = parse(valor_data)
        except (ValueError, TypeError):
            raise DataFormatInvalidError('Data em formato inválido ou Valor de data inválido. Informe uma data EM um formato válido.')
        
        return parsed
    
class ControllerHour:
    """Esta classe é responsável por controlar o carimbo de data e hora.
    """
    def __init__(self, carimbo: Optional[CARIMBO]) -> None:
        self.validador = _ValidateData()
        self._data_tratada = self.validador.validar(carimbo)
        self._data: date
        self._hora: datetime

    
    @property
    def carimbo(self) -> str:
        return self._carimbo
    
    @property
    def data(self) -> str:
        return self._data
    
    @property
    def hora(self) -> str:
        return self._hora


    
    