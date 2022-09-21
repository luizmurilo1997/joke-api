# JOKE API
A Joke é uma API REST gratuita para fatos sobre Chuck Norris.

## ⚙️ Requisitos

Recomendado (principalmente para desenvolvimento local):
- [Python 3.9](https://www.python.org/)
- [Docker\*](https://www.docker.com/)

## 🏃🏽‍♂️ Rodando local com docker

Para rodar o projeto localmente basta docker-compose up --build

## Rodando local sem docker (Windows)

python -m venv .venv

Se Windows:
    .venv/Scripts/activate
Se Linux ou Mac:
    source .venv/bin/activate

uvicorn --app-dir src app:app --reload

Após a execução, a documentação da API ficará disponível localmente no endereço http://localhost:8008/docs
