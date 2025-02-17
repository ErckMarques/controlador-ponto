# HControll CLI

Este projeto é uma CLI criada para controle interno/pessoal da horas trabalhadas.

O programa é desenvolvido em python 3.12 com bibliotecas nativas, como `argparser, datetime e sqlite3` e a biblioteca externa  `dateparser`.

## Motivação

 A  motivação primordial desta aplicação é ter uma ferramenta para saber quantas horas de trabalho estou cumprindo a cada dia.

Também será um ótimo exercício para aprender a:

* Construir documentações com `MkDocs + python3`
* Entender como empacotar aplicações python com `setuptools`
* Utilizar a ferramenta de controle `git` para versionar o código.

## Instalação

### Baixe os arquivos do repositório

Se você utiliza o git faça o clone do repositório. Em seu terminal vá até uma pasta de sua escolha e faça o clone do repositorio, como no exemplo abaixo:

```bash
cd C:/users/projetos_python
git clone https://github.com/ErckMarques/controlador-ponto.git
```

Se você não utiliza o git, acesse o link: [https://github.com/ErckMarques/controlador-ponto.git](https://github.com/ErckMarques/controlador-ponto.git%E2%80%B8) e baixe todos os arquivos para a sua maquina.

Com os arquivos baixados podemos seguir para a instalação

### Instalando a CLI

Recomendo a instalação via pipx.

Se você ainda não tem pipx instalado na sua máquina, com o seu interpretador python global ativado, digite no prompt de comando:

```cmd
python -m pip install --user pipx
python -m pipx ensurepath
```

Em seguida, certifique-se de que está dentro do diretorio raiz do projeto (o mesmo diretorio onde está o arquivo setup.py) e execute:

```
pipx install .
```

Isto é suficiente para que a CLI já possa ser acessada, a partir de qualquer caminho no terminal. Isto só é possível porquê você executou o comando `python -m pip install ensurepath` que nos garante que os executáveis sejam colocados no Path do  sistema.

#### Problema a corrigir

Mesmo após instalar só é possível utilizar a CLI com o comando `pip -m controle [options]`

## Próximas Features

* [ ] Suporte a controle de novas atividades, e.g.:

  Controle de tempo de estudos

  Controle de tempo de Tarefas do lar

  Controle de tempo de cozinha
* [ ] Instalação com outras ferramentas como:

  poetry

  pipenv
* [ ] Criação de uma GUI com Tkinter.
