import tkinter as tk
from tkinter import messagebox
import random

def iniciar_jogo():
    global numero, tentativas
    numero = random.randint(1, 100)
    tentativas = 0
    label_resultado.config(text="")
    entrada_palpite.delete(0, tk.END)

def verificar_palpite():
    global tentativas
    try:
        palpite = int(entrada_palpite.get())
        tentativas += 1

        if palpite < numero:
            label_resultado.config(text="Muito baixo!")
        elif palpite > numero:
            label_resultado.config(text="Muito alto!")
        else:
            messagebox.showinfo("Parabéns!", f"Acertou em {tentativas} tentativas!")
            iniciar_jogo()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

janela = tk.Tk()
janela.title("Jogo de Adivinhação")

label_instrucoes = tk.Label(janela, text="Adivinhe o número entre 1 e 100!", font=("Arial", 14))
label_instrucoes.pack(pady=10)

entrada_palpite = tk.Entry(janela, font=("Arial", 12))
entrada_palpite.pack(pady=5)

botao_verificar = tk.Button(janela, text="Verificar", command=verificar_palpite, font=("Arial", 12))
botao_verificar.pack(pady=5)

label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", command=iniciar_jogo, font=("Arial", 12))
botao_reiniciar.pack(pady=5)

iniciar_jogo()

janela.mainloop()