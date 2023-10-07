from tkinter import*
from firebase import firebase
from simplecrypt import encrypt, decrypt


firebase = firebase.FirebaseApplication("https://cifrado-eff67-default-rtdb.firebaseio.com/", None)

root=Tk()
root.title("Sifrado")
root.geometry("400x400")
root.configure(background= "black")

username = '' 
your_code = '' 
your_friends_code = '' 
message_text = '' 
message_entry = ''

def sendData():
    global username
    global your_code
    global message_entry
    
    message = username + " : "+ message_entry.get()
    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()
    put_date = firebase.put("/",your_code, hex_string)
    print(put_date)
    
    
def enterRoom():
    global username
    global your_code
    global your_friends_code
    global message_text
    global message_entry
    
    username = username_entry.get()
    your_code = your_code_entry.get()
    your_friends_code = friends_code_entry.get()
    
    root.destroy()
    
    message_root=Tk()
    message_root.title("Sifrado")
    message_root.geometry("400x400")
    message_root.configure(background= "black")
    
    message_text = Text(message_root, height=20, width=72) 
    message_text.place(relx=0.5,rely=0.35, anchor=CENTER) 
    
    message_label = Label(message_root, text="Mensaje " , font = 'arial 13', bg='#AFC1D6', fg="white") 
    message_label.place(relx=0.3,rely=0.8, anchor=CENTER)
    
    message_entry = Entry(message_root, font = 'arial 15') 
    message_entry.place(relx=0.6,rely=0.8, anchor=CENTER) 
    
    btn_send = Button(message_root, text="Enviar", font = 'arial 13', bg="#D6CA98", fg="black",command=sendData, padx=10, relief=FLAT) 
    btn_send.place(relx=0.5,rely=0.9, anchor=CENTER) 
    
    message_root.mainloop()

username_label = Label(root, text="Nombre de usuario: " , font = 'arial 13', bg ='#AB92BF', fg="white") 
username_label.place(relx=0.2,rely=0.3, anchor=CENTER) 

username_entry = Entry(root) 
username_entry.place(relx=0.6,rely=0.3, anchor=CENTER) 

your_code_label = Label(root, text="Tu código: " , font = 'arial 13', bg ='#AB92BF', fg="white") 
your_code_label.place(relx=0.3,rely=0.4, anchor=CENTER) 

your_code_entry = Entry(root) 
your_code_entry.place(relx=0.6,rely=0.4, anchor=CENTER) 

friends_code_label = Label(root, text="Código de tu amigo: " , font = 'arial 13', bg ='#AB92BF', fg="white") 
friends_code_label.place(relx=0.22,rely=0.5, anchor=CENTER) 

friends_code_entry = Entry(root) 
friends_code_entry.place(relx=0.6,rely=0.5, anchor=CENTER) 

btn_start = Button(root, text="Iniciar" , font = 'arial 13' , bg="#CEF9F2", fg="black",command=enterRoom , relief=FLAT, padx=10) 
btn_start.place(relx=0.5,rely=0.65, anchor=CENTER)

root.mainloop()