import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota = entry_nota.get()
    if nota.replace(".","",1).isdigit():
        notav = float(nota)

        if (notav >= 7):
            resultado = 'Aprovado !'
        elif (notav >= 5):
            resultado = 'Recuperação !'
        else :
            resultado = 'Reprovado !'

        messagebox.showinfo('Resultado', f'Situação: {resultado}')
    else:
        messagebox.showinfo('Erro', ' Digite um número válido')

root = tk.Tk()
root.title('Verificação de Nota')
root.geometry('300x200')
root.configure(bg="#252525")

tk.Label(root, text='Digite a nota do aluno:', bg="#151515", fg='white', font=('Arial',11,'bold')).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(root,text='Verificar', command=verificar_nota, bg="gray", fg='white', font=('Arial',11,'bold')).pack(pady=15)

root.mainloop()
