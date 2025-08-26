import tkinter as tk
from tkinter import messagebox

def verifica_nota():
    nota = entry_nota.get()

    if nota.replace(".","",1).isdigit():
        notav = float(nota)
        if notav == 10:
            resultado = 'Perfeito! Nota Maxima!'
        elif notav >= 9 and notav <= 9.9:
            resultado = 'Exelente! Nota Boa!'
        elif notav < 9 and notav >= 5:
            resultado = 'Bom! Nota legal!'
        elif notav >= 0 and notav < 5:
            resultado = ':( Infelizmente não conseguiu!)'
        messagebox.showinfo('Resultado', f'Situação {resultado}')
    else:
        messagebox.showerror('ERRO','Digite um número Valido')
root = tk.Tk()
root.title('Verificação de Nota')
root.geometry('300x200')
root.configure(bg="#252525")

tk.Label(root, text='Digite a nota do aluno:', bg="#151515", fg='white', font=('Arial',11,'bold')).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(root,text='Verificar', command=verifica_nota, bg="gray", fg='white', font=('Arial',11,'bold')).pack(pady=15)

root.mainloop()