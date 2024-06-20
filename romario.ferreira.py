# Importação das bibliotecas
import requests

# Acesso ao site para saber a cotação do dólar em reais
url_dolar = 'https://dolarhoje.com.br/'
response_dolar = requests.get(url_dolar)
html_dolar = response_dolar.text

# Encontrando o índice da string "US$"
pos_usd = html_dolar.find('US$')

# Encontrando a posição da palavra "hoje" a partir do índice encontrado
pos_today = html_dolar.index('hoje', pos_usd)

# Pegando o trecho que fica entre os dois índices
trecho_dolar = html_dolar[pos_usd:pos_today]

# Tratamento dos valores
valor_dolar_str = trecho_dolar[3:8]
valor_dolar_float = float(valor_dolar_str.replace(',', '.'))

valor_real_str = trecho_dolar[41:46]
valor_real_float = float(valor_real_str.replace(',', '.'))


# Acesso ao site para saber a cotação do Bitcoin em dólares
url_bitcoin = 'https://investnews.com.br/cotacao-criptomoeda/btc-bitcoin/'
response_bitcoin = requests.get(url_bitcoin)
html_bitcoin = response_bitcoin.text
 
# Tratamento dos valores
pos_inicial_btc = html_bitcoin.find('BTC')
pos_final_btc = html_bitcoin.index('Dólares', 9931)
trecho_bitcoin = html_bitcoin[pos_inicial_btc:pos_final_btc]

valor_bitcoin_str = trecho_bitcoin[50068:50075]
valor_bitcoin_final = float(valor_bitcoin_str[1:].replace(',', '.'))


# Impressão dos resultados
print(f'1 Bitcoin equivale a R${valor_bitcoin_final * valor_real_float:.2f}')
print(f'1 Bitcoin equivale a US${valor_bitcoin_final:.2f}')
print(f'1 dólar equivale a R${valor_real_float:.2f}')

