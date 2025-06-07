
import streamlit as st
import requests
import time
import datetime
from collections import deque

# === CONFIGURAÇÕES ===
st.set_page_config(page_title="BODINHO - BAC BO", layout="centered", initial_sidebar_state="auto")

# Tema escuro
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #f1f1f1;
    }
    </style>
""", unsafe_allow_html=True)

# Variáveis globais
telegram_token = "8084723198:AAGDxbmNHaRMoJ8k5ciPOhLbRFDUOS0toko"
telegram_chat_id = "-1002740925115"

# Simulação do scraping (depois será substituído pela leitura real do site da Betano)
def simular_resultado():
    import random
    return random.choice(["Player", "Banker", "Tie"])

# Função para enviar alerta via Telegram
def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": mensagem}
    requests.post(url, data=data)

# Detectar padrões nos últimos resultados
def detectar_padroes(lista):
    if len(lista) < 6:
        return

    ultimos = list(lista)[-6:]

    # Alternância de cores
    if all(a != b for a, b in zip(ultimos, ultimos[1:])):
        enviar_telegram("🔁 Alternância detectada no Bac Bo!")

    # Repetições
    if ultimos.count(ultimos[-1]) >= 5:
        enviar_telegram(f"🔥 Repetição de {ultimos[-1]} (5x ou mais)!")

    # Padrões numéricos básicos (exemplo)
    padroes_exemplo = [
        ["Player", "Player", "Banker", "Player", "Player"],
        ["Player", "Player", "Banker", "Banker"],
        ["Banker", "Banker", "Banker", "Player", "Player", "Player"]
    ]

    for padrao in padroes_exemplo:
        if ultimos[-len(padrao):] == padrao:
            enviar_telegram(f"⚠️ Padrão detectado: {padrao}")
            break

# Início do app
st.title("🎲 BODINHO - BAC BO")
st.subheader("Sinais automáticos com scraping e alertas via Telegram")

# Histórico
if "resultados" not in st.session_state:
    st.session_state.resultados = deque(maxlen=100)

# Botão para simular entrada
if st.button("🎯 Adicionar resultado (simulação)"):
    resultado = simular_resultado()
    st.session_state.resultados.append(resultado)
    st.success(f"Resultado adicionado: {resultado}")
    detectar_padroes(st.session_state.resultados)

# Mostrar últimos resultados
st.markdown("### Últimos resultados:")
st.write(list(st.session_state.resultados)[-20:])
import streamlit as st
import requests
import time
import datetime
from collections import deque

# === CONFIGURAÇÕES ===
st.set_page_config(page_title="BODINHO - BAC BO", layout="centered", initial_sidebar_state="auto")

# Tema escuro
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #f1f1f1;
    }
    </style>
""", unsafe_allow_html=True)

# Variáveis globais
telegram_token = "8084723198:AAGDxbmNHaRMoJ8k5ciPOhLbRFDUOS0toko"
telegram_chat_id = "-1002740925115"

# Simulação do scraping (depois será substituído pela leitura real do site da Betano)
def simular_resultado():
    import random
    return random.choice(["Player", "Banker", "Tie"])

# Função para enviar alerta via Telegram
def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": mensagem}
    requests.post(url, data=data)

# Detectar padrões nos últimos resultados
def detectar_padroes(lista):
    if len(lista) < 6:
        return

    ultimos = list(lista)[-6:]

    # Alternância de cores
    if all(a != b for a, b in zip(ultimos, ultimos[1:])):
        enviar_telegram("🔁 Alternância detectada no Bac Bo!")

    # Repetições
    if ultimos.count(ultimos[-1]) >= 5:
        enviar_telegram(f"🔥 Repetição de {ultimos[-1]} (5x ou mais)!")

    # Padrões numéricos básicos (exemplo)
    padroes_exemplo = [
        ["Player", "Player", "Banker", "Player", "Player"],
        ["Player", "Player", "Banker", "Banker"],
        ["Banker", "Banker", "Banker", "Player", "Player", "Player"]
    ]

    for padrao in padroes_exemplo:
        if ultimos[-len(padrao):] == padrao:
            enviar_telegram(f"⚠️ Padrão detectado: {padrao}")
            break

# Início do app
st.title("🎲 BODINHO - BAC BO")
st.subheader("Sinais automáticos com scraping e alertas via Telegram")

# Histórico
if "resultados" not in st.session_state:
    st.session_state.resultados = deque(maxlen=100)

# Botão para simular entrada
if st.button("🎯 Adicionar resultado (simulação)"):
    resultado = simular_resultado()
    st.session_state.resultados.append(resultado)
    st.success(f"Resultado adicionado: {resultado}")
    detectar_padroes(st.session_state.resultados)

# Mostrar últimos resultados
st.markdown("### Últimos resultados:")
st.write(list(st.session_state.resultados)[-20:])
