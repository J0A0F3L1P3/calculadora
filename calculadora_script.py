import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica

# Função para lidar com o clique nos botões de número e operadores
def btn_click(number):
    current = entry.get()  # Obtém o conteúdo atual do campo de entrada
    entry.delete(0, tk.END)  # Limpa o campo de entrada
    entry.insert(0, current + str(number))  # Insere o número ou operador clicado

# Função para limpar o campo de entrada
def btn_clear():
    entry.delete(0, tk.END)

# Função para calcular e exibir o resultado
def btn_equal():
    try:
        result = eval(entry.get())  # Avalia a expressão no campo de entrada
        entry.delete(0, tk.END)  # Limpa o campo de entrada
        entry.insert(0, str(result))  # Insere o resultado no campo de entrada
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Criação da janela principal
root = tk.Tk()
root.title("Calculator")  # Define o título da janela

# Cria um campo de entrada para exibir números e resultados
entry = tk.Entry(root, width=24, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)  # Posiciona o campo de entrada na janela

# Lista de botões e suas posições na calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Criação dos botões e posicionamento na janela
for (text, row, col) in buttons:
    # Cria um botão com o texto 'text'
    btn = tk.Button(root, text=text, width=2, padx=20, pady=20, font=('Arial', 16),
                    command=lambda t=text: btn_click(t) if t != '=' else btn_equal())
    btn.grid(row=row, column=col)  # Posiciona o botão na janela

# Criação do botão de limpar
btn_clear = tk.Button(root, text='C', width=20, padx=20, pady=20, font=('Arial', 16), command=btn_clear)
btn_clear.grid(row=5, column=0, columnspan=4)  # Posiciona o botão de limpar na janela

root.mainloop()  # Inicia o loop principal da interface gráfica