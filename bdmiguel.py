import random

def criar_musica(titulo, artista):
    """
    Essa função cria uma letra de música bem simples.

    Ela usa palavras aleatórias para formar as frases.
    """

    
    palavras = ["alegria", "tristeza", "amor", "amigo", "sonho", "mar", "sol", "lua"]

    
    musica = ""
    musica = musica + titulo + "\n"  
    musica = musica + "Por: " + artista + "\n\n"  

    
    for i in range(5):  
        frase = ""
        for j in range(4):  
            
            palavra_aleatoria = random.choice(palavras)
            frase = frase + palavra_aleatoria + " "  

        
        musica = musica + frase + "\n"

    return musica

def salvar_no_arquivo(musica, nome_do_arquivo):
    """
    Essa função pega a música que criamos e salva num arquivo.
    """
    try:
        arquivo = open(nome_do_arquivo, "w", encoding="utf-8")  
        arquivo.write(musica)  
        arquivo.close()  
        print("Música salva com sucesso!")
    except:
        print("Ocorreu um erro ao salvar a música :(")
        
titulo_da_musica = "Meu Sonho no Mar"
nome_do_artista = "Banda do Miguel"


letra_da_musica = criar_musica(titulo_da_musica, nome_do_artista)


nome_do_arquivo = "minha_musica.txt"


salvar_no_arquivo(letra_da_musica, nome_do_arquivo)

print("Fim do programa!")