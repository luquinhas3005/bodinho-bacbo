import requests
import time
import os
from bs4 import BeautifulSoup
from telegram import Bot

# Configurações do bot
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
URL_BACBO = "https://www.betano.bet.br/casino/live/games/bac-bo/5605/tables/"

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
        print("Erro ao extrair:", e)
    return None

def detectar_padrões(historico):
    sinais = []
    if len(historico) < 5:
        return sinais

    # Exemplo: alternância de cores
    padrao = historico[-3:]
    if padrao[0] != padrao[1] and padrao[1] != padrao[2]:
        sinais.append("Alternância detectada")

    return sinais

def enviar_sinal(mensagem):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=mensagem)
        print("Sinal enviado:", mensagem)
    except Exception as e:
        print("Erro ao enviar sinal:", e)

def principal():
    global último_resultado

    while True:
        resultado = extrair_resultado()

        if resultado and resultado != último_resultado:
            último_resultado = resultado
            resultados.append(resultado)

            sinais = detectar_padrões(resultados)
            for sinal in sinais:
                mensagem = f"🔔 {sinal}\nÚltimo: {resultado}"
                enviar_sinal(mensagem)

        time.sleep(10)

if __name__ == "__main__":
    principal()
