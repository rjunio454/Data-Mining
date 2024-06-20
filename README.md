# Data-Mining
Atividade realiza na solicitada pelo professsor do MBA Data Engineering na matéria de Data Mining e web scraping.
## Entregar um programa em Python (não é no notebook .ipynb) cuja estrutura está no notebook fornecido (desafio).

O programa deve realizar scraping das cotações do bitcoin (em R$) e do dólar (em R$), fazer as conversões de variáveis e a conta do valor do bitcoin em dólares (bitcoin em reais / dolar em reais = bitcoin em dólares).

### Regras:
- Entregar um arquivo com a nomenclatura "seu_nome_sobrenome.py" (exemplo: joao_silva.py)
- Ao executar o programa (`python joao_silva.py`), o programa deve executar e exibir a seguinte mensagem:
  
- Onde:
  - `<valor em reais>` é o valor atual do bitcoin em reais.
  - `<valor em dólares>` é o valor calculado do bitcoin em dólares, usando a cotação atual do dólar em reais.
  - `<cotação 1 dólar>` é o valor atual de 1 dólar em reais.

- Para validação, o código deverá executar e apresentar a resposta requerida.



# Data Mining - Exemplo de Coleta de Dados Financeiros

Este projeto demonstra como coletar informações financeiras da web usando Python e a biblioteca `requests`.

## Objetivo

O objetivo deste script é obter a cotação atual do dólar em reais e a cotação do Bitcoin em dólares. Ele utiliza requisições HTTP para acessar sites que fornecem essas informações e faz o parsing dos dados HTML para extrair as cotações.

## Bibliotecas Utilizadas

- `requests`: Para fazer requisições HTTP.
- `re`: (não utilizado no exemplo final, mas mencionado na versão inicial)

## Como Usar

1. Certifique-se de ter Python instalado no seu sistema.
2. Instale a biblioteca `requests` caso não tenha instalado:
3. Execute o script `data_mining.py`.
4. O resultado será exibido no console, mostrando a conversão de 1 Bitcoin em reais e dólares, além da cotação atual do dólar em reais.


