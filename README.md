ml-uea-cdn
==============================

Projeto Final do módulo de Ciência de Dados para Negócios do Curso de Pós-Graduação em Ciência de Dados da Universidade do Estado do Amazonas (UEA).


# Sobre o projeto

Este projeto tem o objetivo de apresentar o conhecimento adquirido no módulo de Ciência de Dados para Negócios, efetuando uma análise de um problema do mundo real, implementando um modelo de aprendizagem de máquina objetivando resolver este problema e disponibilizando-o através de uma API. 

# Ambiente

Para a implementação deste projeto foram utilizadas a plataforma de conteinerização Docker (https://www.docker.com) e a linguagem de programação Python (https://www.python.org), ressaltando a utilização da biblioteca Flask (https://flask.palletsprojects.com/en/2.0.x/) para montagem dos endpoints e a biblioteca Cookiecutter (https://cookiecutter.readthedocs.io/en/1.7.2/) para organização da estrutura do projeto. Outras bibliotecas podem ser encontradas no arquivo requirements.txt.


# Deployment
## Utilizando o Docker

### Pré-Requisitos

 1. É necessário ter a instalação do software Docker

### Deployment

1. No diretório raiz execute:

        docker build -t ml-uea-cdn --build-arg USERNAME=<seu usuário> --build-arg PASSWORD=<sua senha> . 

2. Em seguida, execute:
    
        docker run -p 5000:5000 ml-uea-cdn 

## Sem a utilização do Docker

### Pré-Requisitos para deployment

 1. De preferência, utilize um ambiente que permita a uitlização de environments. O Anaconda (https://www.anaconda.com) ou o Pyenv (https://github.com/pyenv/pyenv), por exemplo, são boas ferramentas para isso;
 2. No diretório raiz, execute:
    
        pip install -r rquirements.txt --no-cache
        
 3. Em seguida, acesse o diretório /src/app e execute:

        python main.py


