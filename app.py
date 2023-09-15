import tkinter as tk
from tkinter import messagebox

# Palavra para adivinhar
palavra = "PYTHON"

# Variável para rastrear as letras adivinhadas
letras_adivinhadas = []

# Função para verificar se a letra está na palavra
def verificar_letra(letra):
    if letra in letras_adivinhadas:
        messagebox.showinfo("Letra já selecionada", f"A letra '{letra}' já foi selecionada.")
    else:
        letras_adivinhadas.append(letra)
        atualizar_label_palavra()
        if letra in palavra:
            messagebox.showinfo("Adivinhou!", f"A letra '{letra}' está na palavra.")
            if palavra_adivinhada():
                messagebox.showinfo("Parabéns!", "Você adivinhou a palavra corretamente!")
                reiniciar_jogo()
        else:
            messagebox.showinfo("Errou!", f"A letra '{letra}' não está na palavra.")
            tentativas_label.config(text=f"Tentativas restantes: {6 - len(letras_adivinhadas)}")
            if len(letras_adivinhadas) == 6:
                messagebox.showinfo("Fim de jogo", f"Você esgotou suas tentativas. A palavra era {palavra}.")
                reiniciar_jogo()

# Função para atualizar o label da palavra com as letras adivinhadas
def atualizar_label_palavra():
    palavra_exibida = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    label_palavra.config(text=palavra_exibida)

# Função para verificar se a palavra foi completamente adivinhada
def palavra_adivinhada():
    for letra in palavra:
        if letra not in letras_adivinhadas:
            return False
    return True

# Função para reiniciar o jogo
def reiniciar_jogo():
    global letras_adivinhadas
    letras_adivinhadas = []
    tentativas_label.config(text="Tentativas restantes: 6")
    atualizar_label_palavra()
    criar_teclado()

# Função para criar o teclado
def criar_teclado():
    for btn in botoes_teclado:
        btn.config(state=tk.NORMAL, bg="white")

# Configuração da janela
janela = tk.Tk()
janela.title("Jogo da Forca")

# Labels
label_palavra = tk.Label(janela, text="", font=("Arial", 24))
label_palavra.pack(pady=20)

tentativas_label = tk.Label(janela, text="Tentativas restantes: 6", font=("Arial", 12))
tentativas_label.pack()

# Teclado
frame_teclado = tk.Frame(janela)
frame_teclado.pack()

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
botoes_teclado = []

for letra in alfabeto:
    botao = tk.Button(frame_teclado, text=letra, font=("Arial", 12), width=2, height=1,
                      command=lambda l=letra: verificar_letra(l))
    botao.grid(row=0, column=alfabeto.index(letra), padx=2, pady=2)
    botoes_teclado.append(botao)

# Botão de reiniciar
reiniciar_botao = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo, font=("Arial", 12))
reiniciar_botao.pack()

# Inicialização do jogo
reiniciar_jogo()

# Loop principal
janela.mainloop()
