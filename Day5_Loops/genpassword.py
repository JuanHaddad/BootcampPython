import tkinter as tk
import random
# import pyperclip

# Função para gerar a senha e copiá-la para a área de transferência
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = int(letters_entry.get())
    nr_symbols = int(symbols_entry.get())
    nr_numbers = int(numbers_entry.get())

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = ''.join(password_list)

    # Copie a senha para a área de transferência
    pyperclip.copy(password)

    result_label.config(text=f"Senha gerada e copiada: {password}")

# Configurar a janela principal com tamanho de 400x400
root = tk.Tk()
root.title("Password Generator")
root.geometry("200x200")

# Rótulo e entrada para letras
letters_label = tk.Label(root, text="Quantidade de letras:")
letters_label.pack()
letters_entry = tk.Entry(root)
letters_entry.pack()

# Rótulo e entrada para símbolos
symbols_label = tk.Label(root, text="Quantidade de símbolos:")
symbols_label.pack()
symbols_entry = tk.Entry(root)
symbols_entry.pack()

# Rótulo e entrada para números
numbers_label = tk.Label(root, text="Quantidade de números:")
numbers_label.pack()
numbers_entry = tk.Entry(root)
numbers_entry.pack()

# Botão para gerar a senha
generate_button = tk.Button(root, text="Gerar e Copiar Senha", command=generate_password)
generate_button.pack()

# Rótulo para exibir a senha gerada
result_label = tk.Label(root, text="")
result_label.pack()

# Executar a interface gráfica
root.mainloop()
