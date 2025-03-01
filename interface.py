'''
Descrição: Interface para descompactar os arquivos.
'''

import tkinter as tk
from tkinter import filedialog
import descompactar as dc

def selecionar_arquivo():
    filepath = filedialog.askopenfilename(
        filetypes=[("Todos os arquivos", "*.*"), ("Arquivos ZIP", "*.zip"), ("Arquivos TAR.GZ", "*.tar.gz"), ("Arquivos TAR.BZ2", "*.tar.bz2"), ("Arquivos TAR.XZ", "*.tar.xz")]
    )
    entrada_arquivo.delete(0, tk.END)
    entrada_arquivo.insert(0, filepath)

def selecionar_destino():
    destino = filedialog.askdirectory()
    entrada_destino.delete(0, tk.END)
    entrada_destino.insert(0, destino)

def descompactar():
    nome_arq = entrada_arquivo.get()
    destino_arq = entrada_destino.get()
    dc.descompactar_arquivo(nome_arq, destino_arq)
    tk.messagebox.showinfo("Sucesso", "Arquivo descompactado com sucesso!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Descompactador de Arquivos")

# Campo para selecionar o arquivo
tk.Label(janela, text="Arquivo:").grid(row=0, column=0, padx=10, pady=10)
entrada_arquivo = tk.Entry(janela, width=50)
entrada_arquivo.grid(row=0, column=1, padx=10, pady=10)
tk.Button(janela, text="Selecionar", command=selecionar_arquivo).grid(row=0, column=2, padx=10, pady=10)

# Campo para selecionar o destino
tk.Label(janela, text="Destino:").grid(row=1, column=0, padx=10, pady=10)
entrada_destino = tk.Entry(janela, width=50)
entrada_destino.grid(row=1, column=1, padx=10, pady=10)
tk.Button(janela, text="Selecionar", command=selecionar_destino).grid(row=1, column=2, padx=10, pady=10)

# Botão para descompactar
tk.Button(janela, text="Descompactar", command=descompactar).grid(row=2, column=1, padx=10, pady=10)

# Iniciar a interface
janela.mainloop()