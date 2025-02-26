from datetime import datetime, timedelta
from typing import List, Literal, Tuple

from controle.cli import create_parser
from controle.core.model import RecordHour
from controle.cli import tratar_horarios

def main():
    # instancia o parser
    parser = create_parser()
    # lê os argumentos
    args = parser.parse_args()

    # verifica se foi passado um caminho de arquivo
    if args.file is not None:
        # Abre o arquivo 
        with args.file.open(mode='r', encoding='UTF-8') as f:
            # lê seu conteudo
            lines = f.readlines()
            # tratar o conteudo no formato d/m/Y; H:M -> H:M
            lines = [line.strip('\n') for line in lines] #remove quebra de linha
            horarios = tratar_horarios(lines)
        
        # passar os dados para RecordHour
        for h in horarios:
            with RecordHour(carimbo=(h[0], h[1]), tempo=h[-1], user=args.user) as rec:
                rec.insert()
        exit()
    
    # verifica se foi passado algum horario manualmente
    if args.horarios is not None:
        # trata estes horarios
        horarios = tratar_horarios(args.horarios)

        # passa os dados para RecordHour
        for h in horarios:
            with RecordHour(carimbo=(h[0], h[1]), tempo=h[-1], user=args.user) as rec:
                rec.insert()
        exit()
        
    # monto os dados
    inicio = datetime.combine(args.data, args.hora_inicio)
    final = datetime.combine(args.data, args.hora_final)
    tempo = args.hora_final - args.hora_inicio

    # gravo no banco
    with RecordHour(carimbo=(inicio, final), tempo=tempo, user=args.user) as rec:
        rec.insert()

    

if __name__ == '__main__':
    main()