import requests
import time

def checar_btc():
    tentativas = 3  # Número máximo de tentativas
    cont_erro = 0  # contador de tentativas
    while cont_erro < tentativas:
        try:
            url_real = "https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL"
            resposta_real = requests.get(url_real, timeout=10)
            resposta_real.raise_for_status()
            return float(resposta_real.json()['price'])  # Retorna o preço com 2 casas decimais
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API: {e}. Tentando novamente...")
            time.sleep(10)  # Aguarda antes de tentar de novo
            cont_erro += 1  # Incrementa o contador

    print("Falha ao obter o preço após várias tentativas.")
    return None  # Retorna None após todas as tentativas falharem
