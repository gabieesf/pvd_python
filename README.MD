# PDV Lanchonete

Este é um sistema simples de Ponto de Venda (PDV) para uma lanchonete, desenvolvido em Python usando Tkinter para a interface gráfica e SQLite para o banco de dados.

## Pré-requisitos

- Python 3.x instalado (recomendado Python 3.6+)
- Bibliotecas Python necessárias: `tkinter`, `sqlite3`

## Instalação

1. Clone este repositório:

git clone https://github.com/seu-usuario/pdv-lanchonete.git
cd pdv-lanchonete

2. Instale as dependências: pip install -r requirements.txt

## Configuração do Banco de Dados

- O sistema utiliza um banco de dados SQLite (`pdv_lanchonete.db`) que será criado automaticamente ao executar o programa pela primeira vez.

## Execução

Para iniciar o sistema, execute o seguinte comando:

python pdv.py

## Funcionalidades

- **Listar Produtos**: Exibe todos os produtos cadastrados na lanchonete.
- **Registrar Venda**: Permite registrar uma venda de um produto selecionado.
- **Cadastrar Produto**: Adiciona um novo produto ao estoque da lanchonete.
- **Editar Produto**: Permite editar o nome e preço de um produto existente.
- **Deletar Produto**: Remove um produto do estoque da lanchonete.
- **Gerar Relatório de Vendas**: Cria um arquivo CSV com informações detalhadas das vendas realizadas.
