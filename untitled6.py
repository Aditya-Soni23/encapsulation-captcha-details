from tkinter import*
root=Tk()
root.title("Encapsulation")
root.geometry("500x500")
root.configure(bg = "yellow")

label_name = Label(root,text = "Name:")
label_name.place(relx=0.3,rely = 0.1,anchor = CENTER )

input_name = Entry(root)
input_name.place(relx = 0.6,rely = 0.1, anchor = CENTER)

label_passward = Label(root,text = "Passward:")
label_passward.place(relx = 0.3, rely = 0.2,anchor = CENTER)

input_passward = Entry(root)
input_passward.place(relx = 0.6, rely = 0.2, anchor = CENTER)

label_captcha = Label(root,text = "Captcha:")
label_captcha.place(relx = 0.3, rely = 0.3, anchor = CENTER)

input_captcha = Entry(root)
input_captcha.place(relx = 0.6,rely = 0.3, anchor = CENTER)



labeln = Label(root, bg ="yellow")
labeln.place(relx = 0.5, rely = 0.7,anchor = CENTER)

labelp = Label(root, bg ="yellow")
labelp.place(relx = 0.5, rely = 0.8,anchor = CENTER)

labelc = Label(root, bg ="yellow")
labelc.place(relx = 0.5, rely = 0.9,anchor = CENTER)




class userDb():
    def __init__(self):
        self.__username = "Private 🔒"
        self.__passward = "Private 🔒"
        self.captcha = "jp8"
        
    def showUser(self):
        labeln["text"]="name :" + self.__username
        labelp["text"]="passward :"+ self.__passward
        labelc["text"]="captcha :" + self.captcha
        
user = userDb()

def addUser():
     global user
     user.username = input_name.get()
     user.passward = input_passward.get()
     user.captcha = input_captcha.get()

btn_details = Button(root,text = "Update Login Details", command = addUser)
btn_details.place(relx = 0.3,rely =0.5,anchor = CENTER )

btn_profile = Button(root,text = "Show Profile", command = user.showUser)
btn_profile.place(relx= 0.6, rely = 0.5, anchor = CENTER)


root.mainloop()