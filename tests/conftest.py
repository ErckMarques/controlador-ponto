import pytest
from unittest.mock import Mock

@pytest.fixture(scope='module')
def parser():
    """Retorna o parser do módulo controle.cli"""
    
    from controle.cli import create_parser
    
    return create_parser()

@pytest.fixture(scope='module')
def instance(mock: Mock):
    """Retorna uma instancia do banco de dados para teste."""
    mock.patch('controle.')