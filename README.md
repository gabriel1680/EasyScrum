# EasyScrum

Api rest para gestão de projetos ágeis usando scrum

# Features

- Criação de sprints
- Adição de user stories em cada tarefa
- Criação de tarefas para sprint
- Remoção e conclusão de tarefas
- Listagem das sprints e tarefas

## Execução

Criação do ambiente virtual do python

```sh
    python3 -m venv venv
```

### Ativação do venv

- Windows (PowerShell):

```sh
    ./venv/bin/Activate.ps1
```

- MacOS/Linux:

```sh
    source ./venv/bin/activate
```

Instalação das dependências do projeto

```sh
	pip install -r requirements.txt
```

### Criação das variáveis de ambiente

**OBS**: Esse passo é obrigatório para o funcionamento da API, leia com atenção!

Criação do arquivo .env para configuração das variáveis de ambiente

Esse comando vai gerar um .env baseado no env.example por comodidade, mas você pode configurar o arquivo com os valores que quiser, respeitando somente os nomes das variáveis

```sh
    cat .example.env > .env
```

Iniciando o servidor

```sh
    flask run
```
