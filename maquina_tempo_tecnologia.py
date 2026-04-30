import streamlit as st
import random

# 1. BANCO DE DADOS HISTÓRICO
banco_historico = {
    "Evolução da Computação": {
        "1642": {"nome": "Pascaline", "descricao": "Blaise Pascal inventa a Pascaline, a primeira calculadora mecânica do mundo.", "imagem": "imagens/pascaline.jpg"},
        "1837": {"nome": "Máquina Analítica", "descricao": "Charles Babbage projeta o primeiro conceito de um computador programável, enquanto Ada Lovelace escreve o primeiro algoritmo.", "imagem": "imagens/analitica.jpg"},
        "1946": {"nome": "ENIAC (1ª Geração)", "descricao": "Máquinas gigantescas, lentas e que geram muito calor. O ENIAC foi o primeiro computador eletrônico de uso geral.", "imagem": "imagens/eniac.jpg"},
        "1955": {"nome": "A Era dos Transistores", "descricao": "Os transistores substituem as válvulas, tornando os computadores menores, mais rápidos e confiáveis.", "imagem": "imagens/transistor.jpg"},
        "1964": {"nome": "Circuitos Integrados", "descricao": "O uso de chips permite agrupar vários transistores, dando origem aos primeiros sistemas operacionais.", "imagem": "imagens/chip.jpg"},
        "1971": {"nome": "Microprocessadores", "descricao": "A invenção do microprocessador (como o Intel 4004) permite a criação dos computadores pessoais (PCs).", "imagem": "imagens/intel4004.jpg"},
        "1977": {"nome": "O Boom dos PCs", "descricao": "Surgimento de gigantes de garagem. O Apple II e a fundação da Microsoft mudam as regras do jogo.", "imagem": "imagens/apple2.jpg"},
        "1990": {"nome": "Computação Ubíqua", "descricao": "Focada em IA e na World Wide Web, a tecnologia torna-se onipresente na vida diária.", "imagem": "imagens/www.jpg"}
    },
    "A Batalha dos Bits (Videogames)": {
        "1958": {"nome": "Tennis for Two", "descricao": "Criado em um osciloscópio, é considerado um dos primeiros jogos eletrônicos.", "imagem": "imagens/tennis.jpg"},
        "1972": {"nome": "Magnavox Odyssey", "descricao": "O primeiro console doméstico, permitindo jogar na televisão.", "imagem": "imagens/odyssey.jpg"},
        "1978": {"nome": "Space Invaders", "descricao": "Revolucionou os fliperamas e introduziu o conceito de pontuação máxima.", "imagem": "imagens/spaceinvaders.jpg"},
        "1983": {"nome": "O Crash e o Famicom", "descricao": "O mercado americano quebra. No mesmo ano, a Nintendo lança o NES, salvando a indústria.", "imagem": "imagens/nes.jpg"},
        "1990": {"nome": "Guerra dos 16-bits", "descricao": "A rivalidade épica entre Super Nintendo (SNES) e Mega Drive.", "imagem": "imagens/snes.jpg"},
        "1996": {"nome": "Super Mario 64", "descricao": "O grande marco da transição dos jogos para os ambientes 3D.", "imagem": "imagens/mario64.jpg"},
        "2001": {"nome": "Xbox e Halo", "descricao": "A Microsoft entra no mercado e prova que FPS funcionam nos consoles.", "imagem": "imagens/xbox.jpg"},
        "2020": {"nome": "Nova Geração e SSDs", "descricao": "PS5/Xbox Series eliminam telas de carregamento.", "imagem": "imagens/ps5.jpg"}
    },
    "A Computação de Bolso (Celulares)": {
        "1973": {"nome": "A Primeira Ligação", "descricao": "Martin Cooper faz a primeira chamada de um celular portátil de 1 kg.", "imagem": "imagens/cooper.jpg"},
        "1983": {"nome": "DynaTAC 8000X", "descricao": "O primeiro celular comercial. A bateria dura 30 minutos.", "imagem": "imagens/dynatac.jpg"},
        "1990": {"nome": "Motorola PT-550 (Tijolão)", "descricao": "O Brasil homologa seu primeiro celular.", "imagem": "imagens/pt550.jpg"},
        "1993": {"nome": "IBM Simon", "descricao": "O primeiro smartphone. Tela touchscreen monocromática.", "imagem": "imagens/simon.jpg"},
        "1997": {"nome": "Nokia 6110", "descricao": "A Nokia populariza o clássico jogo da cobrinha (Snake).", "imagem": "imagens/nokia6110.jpg"},
        "2000": {"nome": "Era Multimídia e BlackBerry", "descricao": "Primeiro celular com câmera e domínio corporativo.", "imagem": "imagens/blackberry.jpg"},
        "2007": {"nome": "A Revolução do iPhone", "descricao": "A Apple dispensa o teclado físico. Tela multitouch e web.", "imagem": "imagens/iphone.jpg"},
        "2010": {"nome": "Internet Móvel", "descricao": "Avanço do 4G/5G e biometria.", "imagem": "imagens/smartphone.jpg"}
    }
}

curiosidades = [
    "O primeiro mouse de computador foi feito de madeira.",
    "O termo 'bug' surgiu quando uma mariposa ficou presa em um computador da Marinha dos EUA.",
    "O ENIAC pesava cerca de 30 toneladas e ocupava 167 metros quadrados.",
    "A primeira mensagem enviada por e-mail foi 'QWERTYUIOP'.",
    "O Nokia 1100 é o celular mais vendido de todos os tempos.",
    "O primeiro domínio registrado na internet foi 'symbolics.com' em 15 de março de 1985."
]

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Máquina do Tempo SIGEMP", page_icon="⏳", layout="wide")

# 3. BARRA LATERAL (SIDEBAR)
with st.sidebar:
    st.title("📟 Painel de Controle")
    st.markdown("Configure sua viagem no tempo:")
    
    lista_rotas = list(banco_historico.keys())
    rota_escolhida = st.selectbox("Escolha a Rota:", lista_rotas)
    
    anos_disponiveis = sorted(banco_historico[rota_escolhida].keys())
    ano_escolhido = st.selectbox("Escolha o Ano:", anos_disponiveis)
    
    st.divider()
    st.subheader("💡 Você sabia?")
    st.info(random.choice(curiosidades))
    
    if st.button("🚀 Salto Aleatório"):
        # Lógica simples para sugerir um destino surpresa
        r = random.choice(lista_rotas)
        a = random.choice(list(banco_historico[r].keys()))
        st.write(f"Tente viajar para **{a}** na rota **{r}**!")

# 4. ÁREA PRINCIPAL
st.title("⏳ Máquina do Tempo Tecnológica")
st.caption(f"Explorando a Rota: {rota_escolhida}")
st.divider()

destino = banco_historico[rota_escolhida][ano_escolhido]

# Layout de duas colunas para o conteúdo
col_texto, col_img = st.columns([1, 1])

with col_texto:
    st.header(f"📍 {destino['nome']}")
    st.subheader(f"Ano: {ano_escolhido}")
    st.write(destino['descricao'])
    
    # Adicionando um "Status do Sistema" para ficar mais tech
    st.success("Sincronização Temporal: 100%")
    st.code(f"ID_DESTINO: {rota_escolhida[:3].upper()}_{ano_escolhido}", language="bash")

with col_img:
    if "imagem" in destino:
        try:
            st.image(destino["imagem"], caption=f"Registro histórico de {ano_escolhido}", use_container_width=True)
        except FileNotFoundError:
            st.warning("⚠️ Arquivo de imagem não encontrado na pasta local.")

# Rodapé discreto
st.divider()
st.markdown("<center>Desenvolvido por Paulo Dionizio - Faculdade de ADS</center>", unsafe_allow_html=True)