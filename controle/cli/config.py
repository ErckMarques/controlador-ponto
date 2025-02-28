"""
Este módulo contém funções para configurar o parser de linha de comando.
O design da função `init_parser` foi inspirado no pattern `Aplication Factory` usado pela biblioteca `flask` do Python.

O parser é configurado com as seguintes opções:
- --horario: Aceita múltiplos valores no formato "data; hora_inicio -> hora_fim"
- --data, -d: Data no formato usual. Se não for informada, assume a data atual.
- --inicio, -i: Hora de início no formato 'HH:MM'. Se não for informada, assume a hora atual.
- --final, -f: Hora de finalização no formato 'HH:MM'. Se não for informada, assume 13:30.
- --user, -u: Nome do usuário. Se não for informado, assume 'erik'.

    Raises:
        ArgumentTypeError: Erro no nome de usuário.
        FileExistError: Caminho não existente no sistema de arquivos.
        ValueError: Erro ao fazer o parser na string de data.
        ValueError: Erro ao fazer o parser na string de horário.
"""

from argparse import ArgumentParser, ArgumentTypeError
from argparse import ONE_OR_MORE, OPTIONAL
from datetime import datetime, time, timedelta
from pathlib import Path
from typing import List, Literal, Tuple

from dateutil.parser import parse

def tratar_horarios(horarios: List[Literal['dd/mm/yyyy; HH:MM -> HH:MM']]) -> List[Tuple[datetime, datetime, timedelta]]:
    """
    Esta função recebe uma lista de horarios e retorna-os como objetos datetiime.
    """
    from re import compile, Pattern
    from dateutil.parser import parse
    
    tratados: List = list()
    regex_data: Pattern = compile(r'^\d{2}/\d{2}/\d{4}')
    regex_horas: Pattern = compile(r'\d{2}:\d{2}')

    # para cada valor, extraímos a data e o horario
    for hora in horarios:
        data = regex_data.match(hora).group()
        minutos = regex_horas.findall(hora)
        # monta os horarios de inicio e final (data+hora)
        inicio = parse(data + ' ' + minutos[0])
        final = parse(data + ' ' + minutos[-1])
        tratados.append((inicio, final, final - inicio))

    return tratados

def parse_date(date_str: str) -> datetime:
    """
    Converte uma string de data em um objeto datetime.
    """
    parsed_date = parse(date_str)
    if not parsed_date:
        raise ValueError(f"Data inválida: {date_str}")
    return parsed_date

def parse_time(time_str: str) -> time:
    """
    Converte uma string de horário no formato 'HH:MM' em um objeto time.
    """
    try:
        return datetime.strptime(time_str, '%H:%M').time().replace(second=0, microsecond=0)
    except ValueError:
        raise ValueError(f"Horário inválido: {time_str}")

def validate_path(str_path: str) -> Path:
    """
    Esta função valida e verifica a existência do caminho informado.
    """
    parsed = Path(str_path)
    if not parsed.exists():
        raise FileExistsError(f'O caminho: {parsed} não é existente no sistema de arquivos.')
    
    return parsed
    
def validate_username(username: str) -> str:
    """
    Valida o nome de usuário.
    - Deve conter apenas letras, números e underscores.
    """
    import re
    if not re.match(r'^\w+$', username):
        raise ArgumentTypeError(
            "O nome de usuário deve conter apenas letras, números e underscores."
        )
    return username

def init_parser(parser: ArgumentParser) -> None:
    """
    Configura as opções do parser de linha de comando.
    """
    # --horario: Aceita múltiplos valores no formato "data; hora_inicio -> hora_fim"
    parser.add_argument(
        '--horario', 
        type=str, 
        help='''
        Horário completo do dia a ser registrado.
        Este comando pode ser utilizado para registrar varios horários de início e fim de um dia qualquer de trabalho.
        Ex.:
            %(prog)s --horario 16/05/2025; 06:04:35 -> 13:56:41 --horario 16-05-2025; 06:04:35 -> 13:56:41
            %(prog)s --horario 2025/05/16; 06:04:35 -> 13:56:41
            %(prog)s --horario 16/05/2025; 06:04 -> 13:56 --horario 16-05-2025; 06:04 -> 13:56
        ''', 
        nargs=ONE_OR_MORE,  # 1 ou mais argumentos
        action='append',  # Cria uma lista de strings
        default=None,
        dest='horarios'
    )

    # --file: se houverem muitos registros, um caminho de arquivo .txt pode ser informado para que os dados sejam carregados
    parser.add_argument(
        '--file',
        type=validate_path, # converte a string para um objeto path
        help='''
        Caminho para um arquivo .txt que contém horários completos de dias de trabalho.
        Utilitário para quando "--horario" tiver muitos registros a serem computados.
        Ex:
            %(prog)s --file path/to/your/archive.txt
        ''',
        nargs=OPTIONAL, # 0 ou 1 argumento
        default=None,
        dest='file'
    )

    # --data: Data no formato usual. Se não for informada, assume a data atual.
    parser.add_argument(
        '-d', '--data', 
        type=parse_date,  # Converte a string para um objeto datetime
        help='''
        Data a ser registrada.
        Quando não informada, a data padrão é a data de hoje.
        Ex.: 
            %(prog)s -d 15/04/2006 ou %(prog)s --data 15-04-2006
        ''', 
        nargs=OPTIONAL,  # 0 ou 1 argumento
        default=datetime.now(),  # Valor padrão é a data atual
    )

    # inicio: Hora de início no formato 'HH:MM'. Se não for informada, assume a hora atual.
    parser.add_argument(
        '-i','--inicio',   
        type=parse_time,  # Converte a string para um objeto time
        help='''
        Hora de início de trabalho a ser registrada.
        Quando não informada, a hora padrão é a hora atual.
        Ex.: 
            %(prog)s -i 06:10 ou %(prog)s -inicio 06:10
        ''', 
        nargs=OPTIONAL,  # 0 ou 1 argumento
        default=datetime.now().time(),  # Valor padrão é a hora atual
        dest='hora_inicio',
    )

    # final: Hora de finalização no formato 'HH:MM'. Se não for informada, assume 13:30.
    parser.add_argument(
        '-f', '--final', 
        type=parse_time,  # Converte a string para um objeto time
        help='''
        Hora de finalização de trabalho a ser registrada.
        Quando não informada, a hora padrão é 13:30.
        Ex.: 
            %(prog)s -f 18:49 ou %(prog)s --final 18:49
            %(prog)s -f (a hora final será 13:30)
        ''', 
        nargs=OPTIONAL,  # 0 ou 1 argumento
        default=time(13, 30),  # Valor padrão é 13:30
        dest='hora_final',
    )

    # --user: Nome do usuário. Se não for informado, assume 'erik'.
    parser.add_argument(
        '-u', '--user',
        type=validate_username,  # Valida o nome de usuário
        help='Nome do usuário a ser associado ao registro.',
        default='erik',  # Valor padrão é 'erik'
        dest='user',
        metavar='USERNAME',  # Nome do argumento na ajuda
    )

# Exemplo de uso
if __name__ == "__main__":
    parser = ArgumentParser()
    init_parser(parser)
    args = parser.parse_args()

    print("Argumentos processados:")
    print(f"--horario: {args.horario}")
    print(f"--data: {args.data} (tipo: {type(args.data)})")
    print(f"inicio: {args.inicio} (tipo: {type(args.inicio)})")
    print(f"final: {args.final} (tipo: {type(args.final)})")
    print(f"--user: {args.user}")