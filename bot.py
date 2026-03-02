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
        "link": "https://shopee.com.br/Capinha-Silicone-Aveludada-Cor-PRETO-BRANCO-Para-IPhone-7G-8G-X-Xsmax-7Plus-XR-11-13-14-15-15Promax-16-16Promax-i.740987884.19599592120?extraParams=%7B%22display_model_id%22%3A209602968951%2C%22model_selection_logic%22%3A3%7D",
        "imagem": "https://linkdaimagem.com"
    },
    {
        "nome": "Capinha Anti Impacto iPhone 14",
        "preco": "R$ 39,90",
        "link": "https://shopee.com.br/Capinha-Silicone-Aveludada-Cor-PRETO-BRANCO-Para-IPhone-7G-8G-X-Xsmax-7Plus-XR-11-13-14-15-15Promax-16-16Promax-i.740987884.19599592120?extraParams=%7B%22display_model_id%22%3A209602968951%2C%22model_selection_logic%22%3A3%7D",
        "imagem": "https://down-br.img.susercontent.com/file/br-11134207-7r98o-m5c7ur37izbk98@resize_w450_nl.webp"
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
    
    time.sleep(10)  # envia a cada 30 minutos
