import pytest

from argparse import ArgumentParser, ArgumentTypeError
from datetime import datetime, time


def test_conversores_tipos():
    """
    Verifica se os conversores de tipo estão funcionando corretamente.
    """
    from controle.cli.config import parse_date, parse_time, validate_username

    assert parse_date('2021-01-01') == datetime(2021, 1, 1)
    assert parse_date('01/01/2021') == datetime(2021, 1, 1)
    assert parse_time('12:30') == time(12, 30)
    assert validate_username('erik') == 'erik'
    
    # a função validadora permite apenas letras, número e underscore
    with pytest.raises(ArgumentTypeError):
        validate_username('erik@')

def test_valores_parser(parser: ArgumentParser):

    args = parser.parse_args('-d 01/01/2021 --inicio 06:45 --final 21:21'.split())

    assert args.data == datetime(2021, 1, 1)
    assert args.hora_inicio == time(6, 45)
    assert args.hora_final == time(21, 21)


def test_opcao_horario_valor(parser: ArgumentParser):
    
    args = parser.parse_args('--horario 26/02/2025; 07:30 -> 14:23', '--horario 2023-02-25; 07:10 -> 13:30')
    assert len(args.horarios) == 2