from tkinter import Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button, END
import bd as b

tupla_selecionada = None

def get_selecionado(event):
    global tupla_selecionada
    index = lista.curselection()[0]
    tupla_selecionada = lista.get(index)    
    entrada_nome.delete(0, END)
    entrada_nome.insert(END, tupla_selecionada[1])
    entrada_av1.delete(0, END)
    entrada_av1.insert(END, tupla_selecionada[2])
    entrada_av2.delete(0, END)
    entrada_av2.insert(END, tupla_selecionada[3])
    entrada_av3.delete(0, END)
    entrada_av3.insert(END, tupla_selecionada[4])
    entrada_avd.delete(0, END)
    entrada_avd.insert(END, tupla_selecionada[5])
    entrada_avds.delete(0, END)
    entrada_avds.insert(END, tupla_selecionada[6])
    entrada_email.delete(0, END)
    entrada_email.insert(END, tupla_selecionada[7])
    entrada_endereco.delete(0, END)
    entrada_endereco.insert(END, tupla_selecionada[8])
    entrada_campus.delete(0, END)
    entrada_campus.insert(END, tupla_selecionada[9])
    entrada_periodo.delete(0, END)
    entrada_periodo.insert(END, tupla_selecionada[10])

def incluir():
    b.inserir(nome.get(), av1.get(),av2.get(), av3.get(), avd.get(), avds.get(), email.get(), endereco.get(), campus.get(), periodo.get())
    lista.delete(0, END)
    lista.insert(END,(nome.get(), av1.get(), av2.get(), av3.get(), avd.get(), avds.get(), email.get(), endereco.get(), campus.get(), periodo.get()))
    entrada_nome.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    entrada_email.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    exibir()

def exibir():
    lista.delete(0, END)
    for linha in b.view():
        lista.insert(0, linha)

def alterar():
    b.update(tupla_selecionada[0], nome.get(), av1.get(), av2.get(), av3.get(), avd.get(), avds.get(), email.get(), endereco.get(), campus.get(), periodo.get())
    entrada_nome.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    entrada_email.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    exibir()

def excluir():
    b.delete(tupla_selecionada[0])
    entrada_nome.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    entrada_email.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    exibir()

root = Tk()
root.title("++++++++ Cadastro de alunos ++++++++++")
width = 840
height = 280

sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)

root.geometry("%dx%d+%d+%d"%(width, height, x, y))
root.resizable(0,0)
root.geometry("1300x500")
#root.iconbitmap("F:\Temp\Python\Controle_Livro\Agenda\icons8_user.ico")
root.config(bg='#5F9EA0')

label_nome = Label(root, text="Nome", bg='light sky blue', fg="#6006ff")
label_nome.grid(row=0, column=0)
label_av1 = Label(root, text="Av1", bg='light sky blue', fg="#6006ff")
label_av1.grid(row=0, column=2)
label_av2 = Label(root, text="Av2", bg='light sky blue', fg="#6006ff")
label_av2.grid(row=2, column=0)
label_av3 = Label(root, text="Av3", bg='light sky blue', fg="#6006ff")
label_av3.grid(row=2, column=2)
label_avd = Label(root, text="Avd", bg='light sky blue', fg="#6006ff")
label_avd.grid(row=0, column=4)
label_avds = Label(root, text="Avds", bg='light sky blue', fg="#6006ff")
label_avds.grid(row=2, column=4)
label_email = Label(root, text="Email", bg='light sky blue', fg="#6006ff")
label_email.grid(row=0, column=6)
label_endereco = Label(root, text="Endereco", bg='light sky blue', fg="#6006ff")
label_endereco.grid(row=2, column=6)
label_campus = Label(root, text="Campus", bg='light sky blue', fg="#6006ff")
label_campus.grid(row=0, column=8)
label_periodo = Label(root, text="Periodo", bg='light sky blue', fg="#6006ff")
label_periodo.grid(row=2, column=8)



nome = StringVar()
av1 = StringVar()
av2 = StringVar()
av3 = StringVar()
avd = StringVar()
avds = StringVar()
email = StringVar()
endereco = StringVar()
campus = StringVar()
periodo = StringVar()

entrada_nome = Entry(root,  textvariable=nome)
entrada_nome.grid(row=0, column=1)
entrada_av1 = Entry(root,  textvariable=av1)
entrada_av1.grid(row=0, column=3)
entrada_av2 = Entry(root,  textvariable=av2)
entrada_av2.grid(row=2, column=1)
entrada_av3 = Entry(root,  textvariable=av3)
entrada_av3.grid(row=2, column=3)
entrada_avd = Entry(root,  textvariable=avd)
entrada_avd.grid(row=0, column=5)
entrada_avds = Entry(root,  textvariable=avds)
entrada_avds.grid(row=2, column=5)
entrada_email = Entry(root,  textvariable=email)
entrada_email.grid(row=0, column=7)
entrada_endereco = Entry(root,  textvariable=endereco)
entrada_endereco.grid(row=2, column=7)
entrada_campus = Entry(root,  textvariable=campus)
entrada_campus.grid(row=0, column=9)
entrada_periodo = Entry(root,  textvariable=periodo)
entrada_periodo.grid(row=2, column=9)



lista = Listbox(root, height=8, width=60)
lista.grid(row=6, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(root)
sb.grid(row=6, column=2, rowspan=6)

lista.configure(yscrollcommand=sb.set)
sb.configure(command=lista.yview)

lista.bind("<<ListboxSelect>>", get_selecionado)


b1 = Button(root, text="Incluir", width=22, bg="royal blue", command=incluir)
b1.grid(row=5, column=4)
b2 = Button(root, text="Exibir", width=22, bg="snow", command=exibir)
b2.grid(row=6, column=4)
b3 = Button(root, text="Alterar", width=22, bg="snow", command=alterar)
b3.grid(row=5, column=5)
b4 = Button(root, text="Excluir", width=22, bg="firebrick4", command=excluir)
b4.grid(row=6, column=5)
b5 = Button(root, text="Fechar", width=22, bg="red", command=root.destroy)
b5.grid(row=8, column=5)


root.mainloop()


