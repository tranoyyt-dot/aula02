import tkinter as tk
from tkinter import messagebox

user_credentials = {}
def show_login_window():
    register_window.destroy()
    create_login_window()
def register_user():
    username = entry_username_register.get()
    password = entry_password_register.get()
    confirm_password = entry_confirm_password.get()
    if not username or not password or not confirm_password:
        messagebox.showerror("Erro de Registro", "Todos os campos são obrigatórios.")
        return
    elif password != confirm_password:
        messagebox.showerror("Erro de Registro", "As senhas não correspondem.")
        return
    elif username in user_credentials:
        messagebox.showerror("Erro de Registro", "Este nome de usuário já existe.")
        return
    user_credentials[username] = password
    messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
    show_login_window()
def login_user():
    username = entry_username_login.get()
    password = entry_password_login.get()
    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        login_window.destroy()
    else:
        messagebox.showerror("Erro de Login", "Nome de usuário ou senha inválidos.")
def create_register_window():
    global register_window, entry_username_register, entry_password_register, entry_confirm_password
    
    register_window = tk.Tk()
    register_window.title("Janela de Registro")
    register_window.geometry("300x200")

    label_username = tk.Label(register_window, text="Nome de Usuário:")
    label_username.pack()
    entry_username_register = tk.Entry(register_window)
    entry_username_register.pack()

    label_password = tk.Label(register_window, text="Senha:")
    label_password.pack()

    entry_password_register = tk.Entry(register_window, show="*")
    entry_password_register.pack()

    label_confirm_password = tk.Label(register_window, text="Confirmar Senha:")
    label_confirm_password.pack()

    entry_confirm_password = tk.Entry(register_window, show="*")
    entry_confirm_password.pack()

    button_register = tk.Button(register_window, text="Registrar", command=register_user)
    button_register.pack(pady=10)

    register_window.mainloop()

def create_login_window():
    global login_window, entry_username_login, entry_password_login
    login_window = tk.Tk()
    login_window.title("Janela de Login")
    login_window.geometry("300x150")

    label_username = tk.Label(login_window, text="Nome de Usuário:")
    label_username.pack()

    entry_username_login = tk.Entry(login_window)
    entry_username_login.pack()

    label_password = tk.Label(login_window, text="Senha:")
    label_password.pack()

    entry_password_login = tk.Entry(login_window, show="*")
    entry_password_login.pack()

    button_login = tk.Button(login_window, text="Login", command=login_user)
    button_login.pack(pady=10)

    login_window.mainloop()
if __name__ == "__main__":
    create_register_window()
