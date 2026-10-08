import tkinter as tk


def calcular():
    nota1_ = float(nota1.get()) 
    nota2_ = float(nota2.get())
    nota3_ = float(nota3.get())
    media = (nota1_ + nota2_ + nota3_) / 3

    resultado.config(text=media)



janela = tk.Tk()
janela.geometry('500x500')

tk.Label(janela, text= 'SISTEMA DE NOTAS' , font=('arial',15), fg='red').pack(pady = 5)

nota1 = tk.Entry(janela, width=5, font=('arial',15), fg='red')
nota1.pack(pady=5)

nota2 = tk.Entry(janela, width=5, font=('arial',15), fg='red')
nota2.pack(pady=5)

nota3 = tk.Entry(janela,width=5, font=('arial',15), fg='red')
nota3.pack(pady=5)


btn  =  tk.Button(janela, text= 'Calcular', command=calcular, font=('arial', 15))
btn.pack(pady=5)

resultado  =  tk.Label(janela, text= '', font=('arial', 15))
resultado.pack(pady=5)


janela.mainloop()






# # python puro
# while True:
#     print('SISTEMA DE NOTAS ...')
#     nome  =  input('Digite o nome do aluno:')

#     nota1 =  float(input('Nota: '))
#     nota2 =  float(input('Nota: '))
#     nota3 =  float(input('Nota: '))

#     soma = nota1 + nota2 + nota3
#     media = soma/3

#     print('Aluno', nome)
#     print('Média', round(media,2))


#     passou = media >= 7
#     recuperacao = media >=5 and media < 7
#     reprovado = media < 5

#     print('SITUAÇÃO DO ALUNO', nome)

#     print(f''' 

#     Passou de ano?  - {passou}
#     Recuperação?    - {recuperacao}
#     Reprovaodo?     - {reprovado}     

#     ''')



