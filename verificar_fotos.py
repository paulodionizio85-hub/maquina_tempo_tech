import os

# 1. Lista de imagens que o seu código ESPERA encontrar
# (Ajuste os nomes aqui se você mudou algo no dicionário principal)
fotos_esperadas = [
    "pascaline.jpg", "analitica.jpg", "eniac.jpg", "transistor.jpg", 
    "chip.jpg", "intel4004.jpg", "apple2.jpg", "www.jpg",
    "tennis.jpg", "spacewar.jpg", "computerspace.jpg", "odyssey.jpg",
    "pong.jpg", "spaceinvaders.jpg", "pacman.jpg", "nes.jpg",
    "mario.jpg", "snes.jpg", "mario64.jpg", "ff7.jpg",
    "xbox.jpg", "wow.jpg", "wii.jpg", "lol.jpg", "ps5.jpg",
    "cooper.jpg", "dynatac.jpg", "pt550.jpg", "sms.jpg",
    "simon.jpg", "nokia6110.jpg", "blackberry.jpg", "iphone.jpg",
    "htcdream.jpg", "smartphone.jpg"
]

pasta_imagens = "imagens"

print(f"--- Iniciando Auditoria na pasta '{pasta_imagens}' ---\n")

if not os.path.exists(pasta_imagens):
    print(f"❌ ERRO: A pasta '{pasta_imagens}' não foi encontrada!")
else:
    arquivos_na_pasta = os.listdir(pasta_imagens)
    sucesso = 0
    erros = 0

    for foto in fotos_esperadas:
        if foto in arquivos_na_pasta:
            print(f"✅ OK: {foto}")
            sucesso += 1
        else:
            # Tenta ajudar a encontrar se o erro for apenas a extensão (ex: .png em vez de .jpg)
            nome_sem_extensao = foto.split('.')[0]
            sugestoes = [f for f in arquivos_na_pasta if f.startswith(nome_sem_extensao)]
            
            if sugestoes:
                print(f"⚠️ AVISO: '{foto}' não encontrada, mas existe '{sugestoes[0]}'. Ajuste a extensão no código!")
            else:
                print(f"❌ FALTANDO: '{foto}'")
            erros += 1

    print(f"\n--- Resumo ---")
    print(f"Imagens vinculadas: {sucesso}")
    print(f"Imagens com erro/faltando: {erros}")