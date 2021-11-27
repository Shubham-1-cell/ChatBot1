from tkinter import *
from chat import get_response, bot_name


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=500, bg="#000000")

        #head lable
        head_lable = Label(self.window, text="Sam The ChatBot", font=("Comic Sans MS", 12, 'bold'), fg="#C0C0C0", bg="#696969", pady=10)
        head_lable.place(relwidth=1)

        #Divider

        line = Label(self.window, width = 450, bg="#C0C0C0")
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        self.text_widget = Text(self.window, fg="#C0C0C0", bg="#000000",width=20,height=2 ,font=("Comic Sans MS", 12), pady=10)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll bar

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)


        # Bottom lable

        bottom_lable = Label(self.window, bg='#A9A9A9', height=80)
        bottom_lable.place(relwidth=1, rely=0.825)

        # Entry box
        self.msg_entry = Entry(bottom_lable, fg="#000000", bg="#f0f0f0", font=("Comic Sans MS", 12), width=40)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, relx=0.011, rely=0.003)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(bottom_lable, text="Send", bg="#008b8b", fg="#000000", font=("Comic Sans MS", 12, 'bold'), command=lambda: self._on_enter_pressed(None))
        send_button.place(relwidth=0.228, relheight=0.06, relx=0.765, rely=0.003)



    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_msg(msg, "You")
        
    def _insert_msg(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        self.text_widget.see(END)
        



if __name__ == '__main__':
    app = ChatApplication()
    app.run()        