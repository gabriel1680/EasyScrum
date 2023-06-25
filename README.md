# EasyScrum

Api rest para gestão de projetos ágeis usando scrum

# Features

- Criação e conclusão de sprints
- Adição de user stories em cada tarefa
- Criação de tarefas para sprint
- Remoção e conclusão de tarefas
- Listagem das sprints e tarefas

## Execução

Cração do ambiente virtual do python

```sh
make venv
```

Instalação das dependências do projeto

```sh
make install
```

Criação do arquivo .env para configuração das variáveis de ambiente

Esse comando vai gerar um .env baseado no env.example por comodidade, mas você pode configurar o arquivo com os valores que quiser, respeitando somente os nomes das variáveis

```sh
make dev-env
```

Iniciar o web server

```sh
make run
```

