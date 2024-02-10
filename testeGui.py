import tkinter as tk

def calcular_imc():
    # Pegar valores de peso e altura dos campos de entrada
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())
    
    # Calcular IMC = peso / (altura * altura)
    imc = peso / (altura ** 2)
    
    # Atualizar o texto do rótulo de resultado com o valor do IMC
    resultado["text"] = f"Seu IMC é: {imc:.2f}"

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Criar um rótulo e campo de entrada para o peso
rotulo_peso = tk.Label(janela, text="Peso (kg):")
rotulo_peso.pack()

entrada_peso = tk.Entry(janela)
entrada_peso.pack()

# Criar um rótulo e campo de entrada para a altura
rotulo_altura = tk.Label(janela, text="Altura (m):")
rotulo_altura.pack()

entrada_altura = tk.Entry(janela)
entrada_altura.pack()

# Criar um botão para calcular o IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()

# Criar um rótulo para mostrar o resultado
resultado = tk.Label(janela, text="Seu IMC aparecerá aqui.")
resultado.pack()

# Iniciar o loop principal da GUI
janela.mainloop()
