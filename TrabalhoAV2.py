import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import Tk, Label, StringVar, Entry, Button, Frame, Menu, Scrollbar, Toplevel, TOP, X, Y, W, SOLID, LEFT, RIGHT, BOTTOM, HORIZONTAL, VERTICAL, NO


root = Tk()
root.title("LISTA DE CONTATOS")
width = 800
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.iconbitmap('C:\Users\Rafa\PycharmProjects\pythonProject')
root.resizable(0,0)
root.config(bg='#6666ff')


nome = StringVar()
telefone = StringVar()
email = StringVar()
idade = StringVar()
endereco = StringVar()
matricula = None
caminho_db = 'E:\pythonProject\index\contatos.db'
update_window = None
new_window = None


def database():
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS humanos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                idade TEXT,
                email TEXT,
                endereco TEXT
            )'''
    cursor.execute(query)
    cursor.execute('SELECT * FROM humanos ORDER BY nome')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def submit():
    if nome.get() == '' or telefone.get() == '' or idade.get() == '' or email.get() == '' or endereco.get() == '':
        msb.showwarning('', 'Digite todos os campos!', icon='warning')
    else:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        query = 'INSERT INTO humanos (nome, telefone, idade, email, endereco) VALUES (?, ?, ?, ?, ?)'
        cursor.execute(query, (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get())))
        conn.commit()
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()
        nome.set('')
        telefone.set('')
        idade.set('')
        endereco.set('')
        email.set('')

def update():
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    cursor.execute('''UPDATE humanos SET nome = ?, telefone = ?, idade = ?, email = ?, endereco = ? WHERE id =?''',
                   (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()), int(matricula)))
    conn.commit()
    cursor.execute('''SELECT * FROM humanos ORDER BY nome''')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()
    nome.set('')
    telefone.set('')
    idade.set('')
    endereco.set('')
    email.set('')
    update_window.destroy()


def selected(event):
    global matricula, update_window
    selected_item = tree.focus()
    content = (tree.item(selected_item))
    selected_item = content['values']
    id = selected_item[0]
    nome.set('')
    nome.set(selected_item[1])
    telefone.set('')
    telefone.set(selected_item[2])
    idade.set('')
    idade.set(selected_item[3])
    email.set('')
    email.set(selected_item[4])
    endereco.set('')
    endereco.set(selected_item[5])

    update_window = Toplevel()
    update_window.title('ATUALIZAR')
    form_titulo = Frame(update_window)
    form_titulo.pack(side=TOP)
    form_contato = Frame(update_window)
    form_contato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = root.winfo_screenwidth()
    sc_height = root.winfo_screenheight()
    x = (sc_width / 2) - (width / 2)
    y = (sc_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    lbl_title = Label(form_titulo, text='Atualizando contatos', width=200)
    lbl_title.pack(fill=X)
    lbl_nome = Label(form_contato, text='Nome')
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(form_contato, text='Telefone')
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(form_contato, text='Idade')
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(form_contato, text='Email')
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(form_contato, text='Endereco')
    lbl_endereco.grid(row=4, sticky=W)

    ent_nome = Entry(form_contato, textvariable=nome)
    ent_nome.grid(row=0, column=1)
    ent_telefone= Entry(form_contato, textvariable=telefone)
    ent_telefone.grid(row=1, column=1)
    ent_idade = Entry(form_contato, textvariable=idade)
    ent_idade.grid(row=2, column=1)
    ent_email = Entry(form_contato, textvariable=email)
    ent_email.grid(row=3, column=1)
    ent_endereco = Entry(form_contato, textvariable=endereco)
    ent_endereco.grid(row=4, column=1)

    btn_atualizar = Button(form_contato, text='Atualizar', width=50, command=update())
    btn_atualizar.grid(row=6,columnspan=2)


def insert():
    global new_window
    nome.set('')
    telefone.set('')
    idade.set('')
    email.set('')
    endereco.set('')

    new_window = Toplevel()
    new_window.title('CADASTRO')
    form_titulo = Frame(new_window)
    form_titulo.pack(side=TOP)
    contact = Frame(new_window)
    contact.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = root.winfo_screenwidth()
    sc_height = root.winfo_screenheight()
    x = (sc_width / 2) - (width / 2)
    y = (sc_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    lbl_title = Label(form_titulo, text='Inserindo contatos', width=200)
    lbl_title.pack(fill=X)
    lbl_nome = Label(form_contato, text='Nome')
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(form_contato, text='Telefone')
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(form_contato, text='Idade')
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(form_contato, text='Email')
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(form_contato, text='Endereco')
    lbl_endereco.grid(row=4, sticky=W)

    ent_nome = Entry(form_contato, textvariable=nome)
    ent_nome.grid(row=0, column=1)
    ent_telefone= Entry(form_contato, textvariable=telefone)
    ent_telefone.grid(row=1, column=1)
    ent_idade = Entry(form_contato, textvariable=idade)
    ent_idade.grid(row=2, column=1)
    ent_email = Entry(form_contato, textvariable=email)
    ent_email.grid(row=3, column=1)
    ent_endereco = Entry(form_contato, textvariable=endereco)
    ent_endereco.grid(row=4, column=1)

    btn_atualizar = Button(form_contato, text='Cadastrar', width=50, command=submit)
    btn_atualizar.grid(row=6, columnspan=2)


def delete():
    if not tree.selection():
        msb.showwarning('', 'Por favor, selecione um item da lista', icon='warning')
    else:
        resultado = msb.askquestion('', 'Tem certeza que deseja excluir o contato?')
        if resultado == 'yes':
            selected_item = tree.focus()
            content = (tree.item(selected_item))
            selected_item = content['values']
            tree.delete(selected_item)
            conn = sqlite3.connect(caminho_db)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM humanos WHERE id = {selected_item[0]}')
            conn.commit()
            cursor.close()
            conn.close()


top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg='#6666ff')
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT)
midleftPadding = Frame(mid, width=300, bg='#6666ff')
midleftPadding.pack(side=LEFT)
midright = Frame(mid, width=100)
midright.pack(side=RIGHT)
bottom = Frame(root, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=300)
tableMargin.pack(side=TOP)


lbl_titulo = Label(top, text='SISTEMA DE CONTATOS', width=500)
lbl_titulo.pack(fill=X)

lbl_alterar = Label(bottom, text='Para alterar clique duas vezes no contato desejado!', width=500)
lbl_alterar.pack(fill=X)


bttn_incluir = Button(midleft, text='INSERIR', bg='royal blue', command=submit)
bttn_incluir.pack()


bttn_excluir = Button(midleft, text='EXCLUIR', bg='OrangeRed2', command=delete)
bttn_excluir.pack()

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=('ID', 'Nome', 'Telefone', 'Idade', 'Email', 'Endereco'),
                    height=400, selectmode='extended', yscrollcommand=ScrollbarY.set, xscrollcommand=ScrollbarX.set)
ScrollbarY.config(command=tree.yview())
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview())
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading('ID', text='ID', anchor=W)
tree.heading('Nome', text='Nome', anchor=W)
tree.heading('Idade', text='Idade', anchor=W)
tree.heading('Telefone', text='Telefone', anchor=W)
tree.heading('Email', text='Email', anchor=W)
tree.heading('Endereco', text='Endereco', anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('Dobule-Button-1', selected)


menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_arquivo = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Menu',menu=menu_arquivo)
menu_arquivo.add_command(label='Criar novo', command=submit)
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Sair', command=root.destroy)

menu_sobre = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Sobre',menu=menu_sobre)

if __name__ == '__main__':
    database()
    root.mainloop()
#Integrantes:
#Daniel Machado Carvalho-202003019241
#Artur Borges de oliveira-202008058287
#Rafael de Ara??jo Almeida-202102444471
