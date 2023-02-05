from tkinter import *
from PIL import ImageTk, Image
from chat import get_response, bot_name
#import tkfont as font
#root = tk()

#Colors
BG_BLACK = "#282828"
BG_BLUEBLACK = "#323232"
BG_GRAY = "#ABB2B9"
BG_YELLOW = "#F4B87F"
BG_BLUE = "#17202A"
BG_PINK = "#D2A5A1"
BG_LIGHTYELLOW = "#FAF8F7"
BG_LIGHTBLUE = "#A9CCD7"
BG_WHITE = "#FEFFFF"
BG_LIGHTORANGE = "#FAECD8"

#Images#
# serene_image = PhotoImage(file = '//Users//manikanta///Downloads//serenelogo.png')


#Text
TEXT_COLOUR = "#000000"
TEXT_REDCOLOR = "#EE2727"


FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    #upper text widget
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=750, bg=BG_BLUEBLACK)

        # head label logo image------------------
        image1 = Image.open("./serenelogo.png")

        newsize = (200, 200)
        image1 = image1.resize(newsize)

        test = ImageTk.PhotoImage(image1)

        label1 = Label(image=test)
        label1.image = test

            # Position image
        label1.place(x= 200, y = -70)

        #send button image-----------------------
        image1 = Image.open("./sendPng.png")

        newsize = (30, 30)
        image1 = image1.resize(newsize)

        test2 = ImageTk.PhotoImage(image1)

        label1 = Label(image=test2)
        label1.image = test2

        # Position image
        #label1.place(x=200, y=-70)



        # frame = Frame(self.window, width=600, height=400)
        # frame.pack()
        # frame.place(anchor='center', relx=0.5, rely=0.5)
        #
        # img = ImageTk.PhotoImage(Image.open('./serenelogo.png'))
        # head_label = Label(frame, image=img)
        # head_label.pack()
        # head_label = Label(self.window, bg=BG_BLUE, fg=TEXT_COLOUR,
        #                     text="SERENE", font=FONT_BOLD, pady=10)
        # head_label.place(relwidth=1)

        #text widget Middle
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_LIGHTORANGE, fg=TEXT_COLOUR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.825, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #bottom label
        bottom_label = Label(self.window, bg=BG_BLUE, height=85)
        bottom_label.place(relwidth=1, rely=0.890)

        #message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_LIGHTBLUE, fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.78, relheight=0.03, rely=0.0098, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, image=test2, font=FONT_BOLD, width=20, bg=BG_WHITE,
                             command= lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.83, rely=0.0098, relheight=0.03, relwidth=0.12)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "USER")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)

        msg1 = f"{sender} : {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name} : {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)

        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()