# Classes e objetos do módulo 'core'

O seguinte texto visa fornecer uma breve e clara descrição de como utilizar as classes de fluxo de trabalho, constantes, funções, etc.

## Constantes

Abaixo uma lista das constantes usadas no módulo 'core'. Todas elas podem ser acessadas:

`from controle.core import CONSTANT`

onde `CONSTANT` é o nome da constante que se quer importar.

### INSTANCE_PATH

Constante que armazena o caminho da pasta para o banco de dados da aplicação.

## Classes de trabalho

Abaixo uma lista das classes de trabalho e seus métodos importantes.

### RecordHour

Classe de fluxo de trabalho para gravar os horários no banco de dados.

#### Usage

```
from datetime import datetime

# Exemplo de uso
carimbo = (datetime.now(), datetime.now())  # Início e final
with RecordHour(carimbo) as rh:
    try:
        rh.insert()  # Insere os dados no banco de dados
    except Exception as e:
        print(f"Erro durante a inserção: {e}")

# Recuperando os dados
with connect(INSTANCE_PATH.joinpath('controle.db'), detect_types=True) as con:
    cur = con.cursor()
    cur.execute("SELECT inicio, final FROM horario")
    rows = cur.fetchall()
    for row in rows:
        print(row)  # Saída: (datetime.datetime(...), datetime.datetime(...))
```
