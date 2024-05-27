import tkinter as tk
from tkinter import filedialog
import pygame

class ListaReproducaoForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Reprodução de Música")
        self.geometry("400x300")
        
        self.configure(bg="black") #cor de fundo

        self.lista_reproducao = []
        self.indice_atual = 0
        pygame.init()

        self.adicionar_musica_button = tk.Button(self, text="Adicionar Música", command=self.adicionar_musica)
        self.adicionar_musica_button.pack()

        self.reproduzir_musica_button = tk.Button(self, text="Reproduzir Música", command=self.reproduzir_musica)
        self.reproduzir_musica_button.pack()

        self.parar_musica_button = tk.Button(self, text="Parar Música", command=self.parar_musica)
        self.parar_musica_button.pack()

    def adicionar_musica(self):
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])
        if arquivo:
            self.lista_reproducao.append(arquivo)

    def reproduzir_musica(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        if self.lista_reproducao:
            pygame.mixer.music.load(self.lista_reproducao[self.indice_atual])
            pygame.mixer.music.play()

    def parar_musica(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    app = ListaReproducaoForm()
    app.mainloop()
