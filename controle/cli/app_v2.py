from argparse import ArgumentParser
from datetime import datetime
from dateparser import parse

def parse_date(date_str):
    return parse(date_str)

def parse_time(time_str):
    return datetime.strptime(time_str, '%H:%M:%S').time()

def to_timestamp(dt):
    return int(dt.timestamp())

parser = ArgumentParser(
    prog='HControll',
    description='%(prog)s - Programa de linha de comando para controle pessoal de horas trabalhadas.',
    conflict_handler='resolve',
)

parser.add_argument(
    '--horario', type=str, 
    help='''
    Horário completo do dia a ser registrado.
    Este comando pode ser utilizado para registrar o horário de início e fim de um dia qualquer de trabalho.
    Ex.:
        %(prog)s horario '16/05/2025; 06:04:35 -> 13:56:41'
    ''', 
    nargs='?',
    action='apend',
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

args = parser.parse_args()

# Convertendo strings para datetime
if args.data:
    args.data = parse_date(args.data)
else:
    args.data = datetime.today()

if args.inicio:
    args.inicio = parse_time(args.inicio)
else:
    args.inicio = datetime.now().time()

if args.final:
    args.final = parse_time(args.final)
else:
    args.final = datetime.now().time()

# Convertendo datetime para timestamp
if args.data:
    args.data_timestamp = to_timestamp(args.data)
if args.inicio:
    args.inicio_timestamp = to_timestamp(datetime.combine(args.data, args.inicio))
if args.final:
    args.final_timestamp = to_timestamp(datetime.combine(args.data, args.final))

print(vars(args))