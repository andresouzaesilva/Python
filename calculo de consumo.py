from tkinter import *

gasolina=Tk()

frame = Frame(gasolina)

labelText = StringVar()

# funçao que calcula o consumo
def consumo():
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    lb["text"] = (num1 / num2)

# Label e caixa da entrada de Kms percorridos
Label(gasolina, text="Digite os KMs percorridos").place(x=50, y=40)
num1Entry = Entry(gasolina)
num1Entry.place(x=50, y=60)

# Label e caixa da entrada da quantidade de gasolina colocada
Label(gasolina, text="Quantos litros de gasolina você colocou?").place(x=50, y=80)
num2Entry = Entry(gasolina)
num2Entry.place(x=50, y=100)

# botão calcular
b3= Button(gasolina, width=7, text="Calcular", command=consumo)
b3.place(x=180, y=140)

# Label e caixa do resultado
Label(gasolina, text="Seu veículo faz").place(x=45, y=180)
lb=Label(gasolina, text="")
lb.place(x=120, y=180)
Label(gasolina, text="Kilometros por litro").place(x=180, y=180)



# Título e dimensão da janela
gasolina.title("Calculadora de Consumo de combustível")
gasolina.geometry("310x310")
gasolina.mainloop()