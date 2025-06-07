import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# ✅ Isso precisa estar antes de qualquer outro comando do Streamlit
st.set_page_config(
    page_title="BODINHO - BAC BO",
    layout="centered",
    initial_sidebar_state="auto"
)

# ----------------------------
# Configurações iniciais
# ----------------------------
st.markdown("<h1 style='text-align: center; color: white;'>🎲 BODINHO - BAC BO</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Sinais automáticos via Telegram • Padrões inteligentes • Tema escuro</h4>", unsafe_allow_html=True)

# Emojis personalizados
EMOJIS = {"Player": "🔴", "Banker": "🔵", "Tie": "🟤"}

# Simulação de resultados (modo demo)
if "resultados" not in st.session_state:
    st.session_state.resultados = []

# Função para gerar uma nova rodada simulada (modo demonstração)
def simular_resultado():
    resultado = random.choice(["Player", "Banker", "Tie"])
    st.session_state.resultados.append(resultado)
    return resultado

# Envio de sinal para Telegram
def enviar_sinal(cor, v_mg0, v_mg1, assertividade, red=False):
    token = "8084723198:AAGDxbmNHaRMoJ8k5ciPOhLbRFDUOS0toko"
    chat_id = "-1002740925115"

    if red:
        mensagem = f"{EMOJIS[cor]} SINAL RED ❌\nÚltima entrada: {cor}"
    else:
        mensagem = (
            f"{EMOJIS[cor]} ENTRADA IDENTIFICADA: {cor.upper()}\n\n"
            f"✅ Vitórias sem martingale: {v_mg0}\n"
            f"🌀 Vitórias com martingale: {v_mg1}\n"
            f"📈 Assertividade: {assertividade:.2f}%"
        )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": mensagem})

# Botões manuais
col1, col2, col3 = st.columns(3)
if col1.button("🔄 Resetar"):
    st.session_state.resultados = []
if col2.button("⚡ Forçar rodada"):
    novo = simular_resultado()
    st.success(f"Rodada: {novo}")
if col3.button("🚀 Modo Turbo"):
    for _ in range(10):
        simular_resultado()
    st.success("Modo Turbo ativado")

# Exibir últimas rodadas
st.markdown("---")
st.subheader("📊 Últimos resultados")
st.write(st.session_state.resultados[-20:][::-1])

# Placeholder para padrões detectados
st.markdown("---")
st.subheader("🔍 Padrões Detectados")
st.info("Modo demonstração ativo. Detecção automática de padrões ao vivo será ativada em breve.")

# Exibir rodapé
st.markdown("---")
st.caption("Desenvolvido para uso pessoal | BODINHO - BAC BO")
