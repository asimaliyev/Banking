from tkinter import *
from tkinter import ttk, Button
import tkinter as tk
from PIL import Image, ImageTk
import employer_interface as ei
import client_interface as ci


class Main(tk.Frame): # контейнер для организации объекта и видж внутри окна
    def __init__(self, mscreen): #конструктор класса
        super().__init__(mscreen)
        self.init_main()

    def init_main(self):
        # --- Кнопки главного меню ---
        self.add_img = tk.PhotoImage(file='pictures/login.png')
        btn_log_in = tk.Button(mscreen,  # к какому фрейму принадлежит
                               # text='Authorization',  # текст кнопки
                               image=self.add_img,
                               command=self.open_dialog,  # вызов функции
                               background="#ffffff",
                               activebackground="#ffffff",
                               compound=tk.TOP
                               )
        btn_log_in['border'] = 0  # убрать рамку вокруг кнопки
        btn_log_in.place(x=300, y=450)

        # --- Background photo ---

        self.background = tk.PhotoImage(file='pictures/asanbg.png.')
        label_background = Label(mscreen, image=self.background)
        label_background.lower()
        label_background.pack()

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(mscreen)
        self.init_child()

    def init_child(self):
        self.title('Authorization')
        self.geometry('400x210+675+450')
        self.resizable(False, False)
        self.iconbitmap('pictures/asanicon.ico')

        self.grab_set()
        self.focus_set()

        # --- Background login menu ---
        self.menu_login_bg = ImageTk.PhotoImage(Image.open('pictures/login_menu.png'))
        self.menu_login = Label(self, image=self.menu_login_bg)
        self.menu_login.lower()
        self.menu_login.pack()

        # --- Поля ---
        label_login = tk.Label(self,
                               text='Login',
                               background="#ffffff",
                               activebackground="#ffffff"
                               )
        label_login.place(x=35, y=20)
        label_password = tk.Label(self,
                                  text='Password',
                                  background="#ffffff",
                                  activebackground="#ffffff"
                                  )
        label_password.place(x=35, y=60)
        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x=38, y=40)
        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x=38, y=80)

        # --- Кнопки ---

        self.img_cancel = tk.PhotoImage(file='pictures/exit.png')
        btn_cancel = tk.Button(self,
                               image=self.img_cancel,
                               command=self.destroy,
                               background="#ffffff",
                               activebackground="#ffffff"
                               )
        btn_cancel['border'] = 0
        btn_cancel.place(x=368, y=170)

        self.img_submit = tk.PhotoImage(file='pictures/submit.png')
        btn_submit = tk.Button(self,
                               image=self.img_submit,
                               command=self.destroy_window,
                               background="#ffffff",
                               activebackground="#ffffff",
                               compound=tk.TOP
                               )
        btn_submit.place(x=32, y=130)
        btn_submit['border'] = 0

        client_checkbutton = Radiobutton(self,
                                         text="Client",
                                         value=1,
                                         variable=lang,
                                         background="#ffffff",
                                         activebackground="#ffffff",
                                         padx=0,
                                         pady=0)
        client_checkbutton.place(x=32, y=105)

        employer_checkbutton = Radiobutton(self,
                                           text="Employer",
                                           value=2,
                                           # command=btn_submit,
                                           variable=lang,
                                           background="#ffffff",
                                           activebackground="#ffffff",
                                           padx=0,
                                           pady=0)
        employer_checkbutton.place(x=90, y=105)

    def destroy_window(self):
        if lang.get() == 2:
            mscreen.destroy()
            ei.emscreen = tk.Tk()
            app = ei.Emain(ei.emscreen)
            app.pack()
            ei.emscreen.title("ASAN Bank")
            ei.emscreen.geometry("750x770+500+150")
            ei.emscreen.resizable(False, False)
            ei.emscreen.iconbitmap('pictures/asanicon.ico')

        elif lang.get() == 1:
            mscreen.destroy()
            ci.cmscreen = tk.Tk()
            app = ci.Cmain(ci.cmscreen)
            app.pack()
            ci.cmscreen.title("ASAN Bank")
            ci.cmscreen.geometry("700x700+500+150")
            ci.cmscreen.resizable(False, False)
            ci.cmscreen.iconbitmap('pictures/asanicon.ico')

        else:
            pass


if __name__ == "__main__":
    mscreen = tk.Tk()
    app = Main(mscreen)
    app.pack()
    mscreen.title("ASAN Bank")
    mscreen.geometry("750x770+500+150")
    mscreen.resizable(False, False)
    mscreen.iconbitmap('pictures/asanicon.ico')
    lang = IntVar()

    mscreen.mainloop()
