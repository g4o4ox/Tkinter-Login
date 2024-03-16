from tkinter import *
from tkinter import messagebox
import data
app = Tk ()
def screnn():
    main=Tk()
    main.resizable(False,False)
    main.geometry('530x530')
    lab=Label(main,text='Logado com sucesso').pack()
    main.mainloop()
app.resizable(False,False)
app.geometry("430x315")
lbl=Label(app,text='Tela de Login v:1.2',font='poppins 34').pack()
user_entry=Entry(app)
user_entry.place(x='115',y='120')
pass_entry=Entry(app,show="&")
pass_entry.place(x='115',y='170')
def LoginDatabase():
    User = user_entry.get()
    Password = pass_entry.get()
    data.cursor.execute('''
                   SELECT * FROM user
                   WHERE (user=? AND pass = ?)
                        ''',(User,Password))
    print('User')
    VerifyLogin=data.cursor.fetchone()
    try:
        if (User in VerifyLogin and Password in VerifyLogin):
            app.destroy()
            screnn()        
    except:
        messagebox.showinfo(title='Falha no Login',message='Credencial não encontrada, tente se cadastrar')
def RegisterDatabase():
    User = user_entry.get()
    Password = pass_entry.get()
    data.cursor.execute('''
INSERT INTO user(user,pass) VALUES(?,?);
''',(User,Password))
    if not User or not Password:
        messagebox.showwarning("Falha no Login","Credencial não encontrada")
        return
    data.conn.commit()
    messagebox.showinfo(title='Login Status', message='Cadastro concluido.')
btn=Button(app,text='Login',bg='green',command=LoginDatabase).place(x='115',y='196')
btn = Button(app,text='Registro',bg='red',command=RegisterDatabase).place(x='200',y='196')
app.mainloop ()