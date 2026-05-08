"""
Testa conectividade com APIs externas usadas pelo SGQ (n8n, Trello).
Uso: python api_tester.py
"""
import os
import urllib.request
import urllib.error

N8N_URL = os.getenv("N8N_URL", "http://localhost:5678/healthz")
TRELLO_KEY = os.getenv("TRELLO_KEY", "")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN", "")


def check_n8n():
    print(f"Verificando n8n em {N8N_URL}...")
    try:
        with urllib.request.urlopen(N8N_URL, timeout=5) as resp:
            print(f"  n8n OK — status {resp.status}")
    except urllib.error.URLError as e:
        print(f"  n8n FALHOU — {e.reason}")


def check_trello():
    if not TRELLO_KEY or not TRELLO_TOKEN:
        print("  Trello: credenciais não configuradas (TRELLO_KEY / TRELLO_TOKEN).")
        return
    url = f"https://api.trello.com/1/members/me?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
    print("Verificando autenticação no Trello...")
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            print(f"  Trello OK — status {resp.status}")
    except urllib.error.URLError as e:
        print(f"  Trello FALHOU — {e.reason}")


if __name__ == "__main__":
    check_n8n()
    check_trello()
