"""
Este módulo realiza a configuração do pacote `cli` onde encontra-se o parser da linha de comando.
"""
from argparse import ArgumentParser

from controle.cli import config

def create_parser() -> ArgumentParser:
    """
    Cria um parser de linha de comando para o pacote `cli`.

    Returns:
        ArgumentParser: O parser de linha de comando configurado.
    """
    parser = ArgumentParser(
        prog='HControll',
        description='%(prog)s - Programa de linha de comando para controle pessoal de horas trabalhadas.',
        conflict_handler='resolve',
    )

    # configurando as ocções do parser
    config.init_parser(parser)

    return parser