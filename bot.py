import requests
import time
import os
from bs4 import BeautifulSoup
from telegram import Bot

# Carregar variáveis de ambiente
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
URL_BACBO = os.environ.get("BACBO_URL") or "https://www.betano.bet.br/casino/live/games/bac-bo/5605/tables/"

# Verificação inicial
if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    print("❌ Erro: TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não definido.")
    exit(1)

# Inicializar o bot
bot = Bot(token=TELEGRAM_TOKEN)
resultados = []
último_resultado = None

def extrair_resultado():
    try:
        response = requests.get(URL_BACBO)
        soup = BeautifulSoup(response.text, "html.parser")
        item = soup.select_one('ul > li:nth-child(3) > div')
        if item:
            return item.text.strip()
    except Exception as e:
        print("Erro ao extrair resultado:", e)
    return None

def detectar_padroes(historico):
    sinais = []
    if len(historico) < 5:
        return sinais

    padrao = historico[-3:]
    if padrao[0] != padrao[1] and padrao[1] != padrao[2]:
        sinais.append("🔁 Alternância detectada")

    return sinais

def enviar_sinal(mensagem):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=mensagem)
        print("✅ Sinal enviado:", mensagem)
    except Exception as e:
        print("❌ Erro ao enviar sinal:", e)

def principal():
    global último_resultado

    while True:
        resultado = extrair_resultado()

        if resultado is not None:
            if resultado != último_resultado:
                print("🎲 Novo resultado:", resultado)
                resultados.append(resultado)
                último_resultado = resultado

                sinais = detectar_padroes(resultados)
                for sinal in sinais:
                    mensagem = f"{sinal}\nÚltimo: {resultado}"
                    enviar_sinal(mensagem)
        else:
            print("⚠️ Nenhum resultado encontrado.")

        time.sleep(10)

if __name__ == "__main__":
    principal()
