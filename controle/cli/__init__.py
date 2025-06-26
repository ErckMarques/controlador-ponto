"""
Este módulo realiza a configuração do pacote `cli` onde encontra-se o parser da linha de comando.
"""
import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter, RawTextHelpFormatter

from controle.cli import config
from controle.cli.config import tratar_horarios

def create_parser() -> ArgumentParser:
    """
    Cria um parser de linha de comando para o pacote `cli`.

    Returns:
        ArgumentParser: O parser de linha de comando configurado.
    """
    parser = ArgumentParser(
        prog='HControll',
        description='%(prog)s - Programa de linha de comando para controle pessoal de Atividades',
        epilog=textwrap.dedent('''
            Controle de atividades pessoais, como horas de trabalho, estudos e outras tarefas.
            '''),
        conflict_handler='resolve',
        formatter_class=RawTextHelpFormatter,
    )

    # configurando as opções do parser
    config.init_parser(parser)

    return parser