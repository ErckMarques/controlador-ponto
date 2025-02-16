from argparse import ArgumentParser
from datetime import datetime

from dateparser import parse

parser = ArgumentParser(
    prog='HControll',
    description='%(prog)s - Programa de linha de comando para controle pessoal de horas trabalhadas.',
    conflict_handler='resolve',
)

parser.add_argument(
    'horario', type=datetime, 
    help='''
        Horário completo do dia a ser registrado.  
        Este comando pode ser utilizado para registrar o horário de início e fim de um dia qualquer de trabalho.
        Ex.: 
            %(prog)s horario -d 16/05/2025 -i 06:04:35 -f 13:56:41
    ''', 
    nargs='?', 
    default=parse,
)

# O padrao de data é a data de hoje
parser.add_argument(
    '-d','--data', 
    type=datetime, 
    help='''
        Data a ser registrada separadamente.
        Quando não informada, a data padrão é a data de hoje.
        Ex.: 
            %(prog)s horario -d 15/04/2006 ou %(prog)s horario --data 15-04-2006
    ''', 
    nargs='?', 
    default=datetime.today, 
    const=parse('today')
)

parser.add_argument(
    '-i','--inicio', 
    type=datetime, 
    help='''
        Hora de inicio de trabalho a ser registrada.
        Quando não informada, a hora padrão é a hora atual.
        Ex.: 
            %(prog)s horario -i 06:10:07 ou %(prog)s horario -inicio 06:10:07
    ''', 
    nargs='?', 
    default=datetime.hour, 
    const=parse
)

parser.add_argument(
    '-f','--final', 
    type=datetime, 
    help='''
        Hora de finalização de trabalho a ser registrada.
        Quando não informada, a hora padrão é a hora atual.
        Ex.: 
            %(prog)s horario -f 18:49:23 ou %(prog)s horario -final 18:49:23
    ''', 
    nargs='?', 
    default=datetime.hour, 
    const=parse
)

args = parser.parse_args()

print(vars(args))