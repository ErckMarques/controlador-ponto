from datetime import datetime

from controle.cli import create_parser
from controle.core.model import RecordHour

def main():
    # instancia o parser
    parser = create_parser()
    # le os argumentos
    args = parser.parse_args()
    # monto os dados
    inicio = datetime.combine(args.data, args.hora_inicio)
    final = datetime.combine(args.data, args.hora_final)
    tempo = args.hora_final - args.hora_inicio

    # gravo no banco
    with RecordHour(carimbo=(inicio, final), tempo=tempo, user=args.user) as rec:
        rec.insert()

    

if __name__ == '__main__':
    main()