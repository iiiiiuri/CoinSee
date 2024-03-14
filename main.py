import requests

def get_crypto_info(symbol, currency='usd'):
    url = f'https://api.coingecko.com/api/v3/coins/{symbol}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    crypto_symbol = "crypto-com-chain"  # Símbolo da CRO na CoinGecko
    crypto_info = get_crypto_info(crypto_symbol, 'brl')
    
    if 'error' not in crypto_info:
        name = crypto_info['name']
        current_price = crypto_info['market_data']['current_price']
        market_cap = crypto_info['market_data']['market_cap']['brl']
        volume = crypto_info['market_data']['total_volume']['brl']
        
        print(f"Nome: {name}") 
        print(f"Preço Atual: {current_price['brl']} BRL")
        print(f"Capitalização de Mercado: {market_cap} BRL")
        print(f"Volume de Negociação (24h): {volume} BRL")
    else:
        print("Criptomoeda não encontrada")

if __name__ == "__main__":
    main()