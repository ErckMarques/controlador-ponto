from contextlib import AbstractContextManager
from sqlite3 import connect, Connection, Cursor, Date
from sqlite3 import SQLITE_CONSTRAINT_NOTNULL, SQLITE_CONSTRAINT_PRIMARYKEY
from typing import Self, Optional, Union, Tuple

from controle import INSTANCE_PATH, CARIMBO

class RecordHour(AbstractContextManager):
    """
    Esta classe é responsável por registrar as informações de hora no banco de dados.
    """
    def __init__(self, carimbo: Tuple[CARIMBO], tabela: str = None) -> None:
        self._con: Optional[Connection] = None
        self._cur: Cursor = self.con.cursor()
        self.carimbo = carimbo
        self.tabela = 'horario' if tabela is None else tabela

    @property
    def con(self) -> Connection:
        return self._con
    
    def __del__(self) -> None:
        if self.con is not None:
            self.con.close()
    
    def __enter__(self) -> Self:
        if self.con is None:
            self._con = connect(INSTANCE_PATH.joinpath('controle.db'))

        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.con.commit()
        self.con.close()
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(carimbo={self.carimbo}, tabela={self.tabela})'
    
    def _criar_tabela(self) -> None:
        self._cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.tabela} (
        id INTEGER {SQLITE_CONSTRAINT_PRIMARYKEY} AUTOINCREMENT, 
        inicio timestamp {SQLITE_CONSTRAINT_NOTNULL}, 
        final timestamp {SQLITE_CONSTRAINT_NOTNULL},
        )
        """)

    def connect(self) -> None:
        if self.con is None:
            self._con = connect(INSTANCE_PATH.joinpath('controle.db'))

    def close(self) -> None:
        if self.con is not None:
            self.con.close()
    
    def insert(self) -> None:
        self._cur.execute(f"INSERT INTO {self.tabela} (inicio, final) VALUES (?, ?)", (*self.carimbo,))
