from argparse import ArgumentParser
from datetime import datetime
from dateparser import parse

def parse_date(date_str):
    return parse(date_str)

def parse_time(time_str):
    return datetime.strptime(time_str, '%H:%M:%S').time()

def to_timestamp(dt: datetime) -> int:
    return int(dt.timestamp())

def init_parser(parser: ArgumentParser) -> None:
    """
    Esta função configura as opções do parser de linha de comando para o pacote `cli`.
    Aplicado o pattern Factory Aplication para configurar o parser de linha de comando,
    inspirado na aula <https://youtu.be/-qWySnuoaTM?si=cMB0YpU0GnBmlvrG> 
    """
    parser.add_argument(
        '--horario', type=str, 
        help='''
        Horário completo do dia a ser registrado.
        Este comando pode ser utilizado para registrar o horário de início e fim de um dia qualquer de trabalho.
        Ex.:
            %(prog)s horario '16/05/2025; 06:04:35 -> 13:56:41'
            %(prog)s horario '16-05-2025; 06:04:35 -> 13:56:41'
            %(prog)s horario '2025/05/16; 06:04:35 -> 13:56:41'
        ''', 
        nargs='?',
        action='append',
        default=None,
    )

    parser.add_argument(
        '-d', '--data', 
        type=str, 
        help='''
        Data a ser registrada separadamente.
        Quando não informada, a data padrão é a data de hoje.
        Ex.: 
            %(prog)s -d 15/04/2006 ou %(prog)s --data 15-04-2006
        ''', 
        nargs='?', 
        default=datetime.today().strftime('%Y-%m-%d'), 
        const='today'
    )

    parser.add_argument(
        '-i', '--inicio', 
        type=str, 
        help='''
        Hora de inicio de trabalho a ser registrada.
        Quando não informada, a hora padrão é a hora atual.
        Ex.: 
            %(prog)s -i 06:10:07 ou %(prog)s -inicio 06:10:07
        ''', 
        nargs='?', 
        default=datetime.now().strftime('%H:%M:%S'), 
        const=None
    )

    parser.add_argument(
        '-f', '--final', 
        type=str, 
        help='''
        Hora de finalização de trabalho a ser registrada.
        Quando não informada, a hora padrão é a hora atual.
        Ex.: 
            %(prog)s -f 18:49:23 ou %(prog)s -final 18:49:23
        ''', 
        nargs='?', 
        default=datetime.now().strftime('%H:%M:%S'), 
        const=None
    )