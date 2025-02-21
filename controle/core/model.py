from contextlib import AbstractContextManager
from datetime import datetime
from sqlite3 import connect, Connection, Cursor, Error, register_adapter, register_converter
from sqlite3 import SQLITE_CONSTRAINT_NOTNULL, SQLITE_CONSTRAINT_PRIMARYKEY
from typing import Self, Optional, Union, Tuple

from controle import INSTANCE_PATH, CARIMBO

# Adaptação do tipo CARIMBO para o SQLite
def adapt_carimbo(carimbo: Tuple[CARIMBO]) -> str:
    """
    Adapta um carimbo (tupla de dois timestamps) para uma string no formato SQLite.
    """
    inicio, final = carimbo
    return f"{inicio.isoformat()},{final.isoformat()}"

# Conversão de uma string SQLite para o tipo CARIMBO
def convert_carimbo(value: bytes) -> Tuple[datetime, datetime]:
    """
    Converte uma string SQLite de volta para um carimbo (tupla de dois timestamps).
    """
    inicio_str, final_str = value.decode("utf-8").split(",")
    inicio = datetime.fromisoformat(inicio_str)
    final = datetime.fromisoformat(final_str)
    return (inicio, final)

register_adapter(tuple, adapt_carimbo)
register_converter('CARIMBO', convert_carimbo)

class RecordHour(AbstractContextManager):
    """
    Esta classe é responsável por registrar as informações de hora no banco de dados.
    Ela representa uma linha de informação da tabela. E pode ser utilizada como um gerenciador de contexto.

    Uso:
        >>> horarios: iterable[Carimbo]

        >>> for horario in horarios:
        ...     with RecorHour(horario) as record:
        ...         record.insert()
    """
    def __init__(self, carimbo: Tuple[CARIMBO], tabela: str = None, user: Optional[str] = None) -> None:
        self._con: Optional[Connection] = None
        self._cur: Optional[Cursor] = None
        self.carimbo = carimbo
        self.tabela = 'horario_' if tabela is None else tabela
        self._user = user

    @property
    def con(self) -> Connection:
        return self._con
    
    @property
    def user(self) -> str:
        return self._user
    
    def __del__(self) -> None:
        if self.con is not None:
            self.con.close()
    
    def __enter__(self) -> Self:
        if self.con is None:
            self._con = connect(INSTANCE_PATH.joinpath('controle.db'), detect_types=True)
            self._cur = self.con.cursor()
            self._criar_tabela()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        try:
            if exc_type is None:
                self.con.commit()
        except Error as e:
            print(f"Erro ao commitar: {e}")
        finally:
            if self._cur is not None:
                self._cur.close()
            if self.con is not None:
                self.con.close()
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(carimbo={self.carimbo}, tabela={self.tabela + self.user})'
    
    def _criar_tabela(self) -> None:
        """Cria uma nova tabela no banco de dados com um nome de tabela fornecido no construtor da classe RecorHour"""
        self._cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.tabela} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        inicio TIMESTAMP NOT NULL, 
        final TIMESTAMP NOT NULL
        )
        """)

    def connect(self) -> None:
        if self.con is None:
            self._con = connect(INSTANCE_PATH.joinpath('controle.db'))
            self._cur = self._con.cursor()
            self._criar_tabela()

    def close(self) -> None:
        if self.con is not None:
            if self._cur is not None:
                self._cur.close()
            self.con.close()
    
    def insert(self) -> None:        
        try:
            self._cur.execute(f"INSERT INTO {self.tabela} (inicio, final) VALUES (?, ?)", (*self.carimbo,))
        except Error as e:
            if e.sqlite_errorcode == SQLITE_CONSTRAINT_NOTNULL:
                print("Erro: Tentativa de inserir um valor nulo em uma coluna NOT NULL.")
            elif e.sqlite_errorcode == SQLITE_CONSTRAINT_PRIMARYKEY:
                print("Erro: Violação de chave primária (valor duplicado).")
            else:
                print(f"Erro ao inserir dados: {e}")
