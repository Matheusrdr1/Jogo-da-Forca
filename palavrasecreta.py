import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "inteligencia"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("*", end=" ")
    print()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    exibir_palavra(palavra_secreta, letras_corretas)

    while True:
        letra_digitada = input("Digite uma letra: ").lower()

        if letra_digitada.isalpha() and len(letra_digitada) == 1:
            if letra_digitada in letras_corretas:
                print("Você já tentou essa letra. Tente outra.")
            elif letra_digitada in palavra_secreta:
                letras_corretas.append(letra_digitada)
                print("Letra correta!")
            else:
                tentativas += 1
                print("Letra errada. Tente novamente.")
            
            exibir_palavra(palavra_secreta, letras_corretas)

            if set(letras_corretas) == set(palavra_secreta):
                print(f"Parabéns! Você acertou a palavra '{palavra_secreta}'.")
                break
        else:
            print("Por favor, digite apenas uma letra válida.")

if __name__ == "__main__":
    jogar_forca()

