import random

def criar_musica(titulo, artista):
    """
    Essa função cria uma letra de música bem simples.

    Ela usa palavras aleatórias para formar as frases.
    """

    # Aqui estão as palavras que vamos usar
    palavras = ["alegria", "tristeza", "amor", "amigo", "sonho", "mar", "sol", "lua"]

    # Vamos começar a música
    musica = ""
    musica = musica + titulo + "\n"  # Adiciona o título
    musica = musica + "Por: " + artista + "\n\n"  # Adiciona o artista

    # Agora vamos criar as frases da música
    for i in range(5):  # Vamos criar 5 frases
        frase = ""
        for j in range(4):  # Cada frase terá 4 palavras
            # Escolhe uma palavra aleatória da nossa lista
            palavra_aleatoria = random.choice(palavras)
            frase = frase + palavra_aleatoria + " "  # Adiciona a palavra na frase

        # Adiciona a frase na música, e pula uma linha
        musica = musica + frase + "\n"

    return musica

def salvar_no_arquivo(musica, nome_do_arquivo):
    """
    Essa função pega a música que criamos e salva num arquivo.
    """
    try:
        arquivo = open(nome_do_arquivo, "w", encoding="utf-8")  # Abre o arquivo para escrever
        arquivo.write(musica)  # Escreve a música no arquivo
        arquivo.close()  # Fecha o arquivo
        print("Música salva com sucesso!")
    except:
        print("Ocorreu um erro ao salvar a música :(")

# *** Programa Principal ***

# Aqui dizemos o nome da música e o artista
titulo_da_musica = "Meu Sonho no Mar"
nome_do_artista = "Banda do Miguel"

# Criamos a música chamando a função
letra_da_musica = criar_musica(titulo_da_musica, nome_do_artista)

# Dizemos o nome do arquivo onde vamos salvar a música
nome_do_arquivo = "minha_musica.txt"

# Salvamos a música no arquivo
salvar_no_arquivo(letra_da_musica, nome_do_arquivo)

print("Fim do programa!")