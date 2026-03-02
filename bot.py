import telegram
import time
import random

TOKEN = "8083548447:AAFex_c9ry6EIhtYyzAzbwwWhoBCOr-Y7l0"
CHAT_ID = "-1003857832192"

bot = telegram.Bot(token=TOKEN)

produtos = [
    {
        "nome": "Capinha Transparente iPhone 13",
        "preco": "R$ 29,90",
        "link": "SEU_LINK_AFILIADO_AQUI",
        "imagem": "https://linkdaimagem.com"
    },
    {
        "nome": "Capinha Anti Impacto iPhone 14",
        "preco": "R$ 39,90",
        "link": "SEU_LINK_AFILIADO_AQUI",
        "imagem": "https://linkdaimagem.com"
    }
]

while True:
    produto = random.choice(produtos)
    
    mensagem = f"""
🔥 OFERTA DO DIA 🔥

📱 {produto['nome']}
💰 {produto['preco']}

🛒 Compre aqui:
{produto['link']}
    """

    bot.send_photo(chat_id=CHAT_ID, photo=produto['imagem'], caption=mensagem)
    
    time.sleep(1800)  # envia a cada 30 minutos
