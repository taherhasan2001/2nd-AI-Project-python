from tkinter import *
from AI import Module
from tkinter import ttk
import os
import webbrowser
# NOTE don't forget to change your resolution to 1600 x 900
path = os.getcwd() + '\imgs'
def callback(url):
   webbrowser.open_new_tab(url)

class interface:
    def __init__(self):
        self.button=None
        self.window = Tk()
        self.canvas = None
        self.entry0 = None
        self.file = False
        self.win = None
        self.selected = 0  # 0 ==> Decision trees // 1 ==> Naïve Bayes // 2 ==> neural network

    def convert(self, selected: int):
        self.selected = selected
        self.canvas.destroy()
        window = self.window
        window.bind('<Return>', self.Enter)
        window.geometry("1600x900")
        window.bind('<Escape>', self.exit)
        window.configure(bg="#ffffff")
        self.canvas = Canvas(window, bg="#ffffff", height=900, width=1600, bd=0, highlightthickness=0, relief="ridge")
        canvas = self.canvas
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=path + r"\backgroundFLOWER.png")
        background = canvas.create_image(800.0, 450.0, image=background_img)

        img0 = PhotoImage(file=path + r"\img3.png")
        b0 = Button(bg='#0C1207', image=img0, borderwidth=0, highlightthickness=0, command=lambda: self.start(),
                    relief="flat")

        b0.place(x=1121.0, y=195.0, width=40, height=40)

        textimg = PhotoImage(file=path + r"\textImage.png")
        textButton = Button(bg='#0C1207', image=textimg, borderwidth=0, highlightthickness=0,
                            command=lambda: self.selectFile(),
                            relief="flat")
        textButton.place(x=451, y=329)
        fileimg = PhotoImage(file=path + r"\fileImage.png")
        fileButton = Button(bg='#0C1207', image=fileimg, borderwidth=0, highlightthickness=0,
                            command=lambda: self.selectFile(file=True),
                            relief="flat")
        fileButton.place(x=451, y=183)
        window.mainloop()
    def contact(self):
        window = self.window
        background_img = PhotoImage(file=path + r"\contactBackground.png")
        contactImg = PhotoImage(file=path + r"\contactButton1.png")
        canvas=self.canvas
        canvas.create_image(800.0, 450.0, image=background_img)
        self.button.configure(image=contactImg,bg='#756340',command=lambda :self.start())
        link = Label(window, bg='#705B39',text="Taher Hasan", font=('Helveticabold', 20), fg="gold", cursor="hand2")
        link.place(x=121,y=270)
        link.bind("<Button-1>", lambda e:
        callback("https://www.facebook.com/profile.php?id=100009133824763"))

        link1 = Label(window, bg='#705B39', text="Saleh Khatib", font=('Helveticabold', 20), fg="gold",
                     cursor="hand2")
        link1.place(x=121, y=381)
        link1.bind("<Button-1>", lambda e:
        callback("https://www.facebook.com/profile.php?id=100006492466238"))

        link2 = Label(window, bg='#705B39', text="Dia Tahboub", font=('Helveticabold', 20), fg="gold",
                      cursor="hand2")
        link2.place(x=121, y=509)
        link2.bind("<Button-1>", lambda e:
        callback("https://www.facebook.com/profile.php?id=100008390258913"))



        window.mainloop()
    def start(self):


        window = self.window
        window.geometry("1600x900")
        window.attributes('-fullscreen', True)
        window.bind('<Escape>', self.exit)
        window.configure(bg="#ffffff")
        self.canvas = Canvas(window, bg="#ffffff", height=900, width=1600, bd=0, highlightthickness=0, relief="ridge")
        canvas = self.canvas
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=path + r"\background.png")
        img0 = PhotoImage(file=path + r"\img0.png")
        img1 = PhotoImage(file=path + r"\img1.png")
        img2 = PhotoImage(file=path + r"\img2.png")  # 0 ==> Decision trees // 1 ==> Naïve Bayes // 2 ==> neural network
        img3 = PhotoImage(file=path + r"\img3.png")
        contactImg = PhotoImage(file=path + r"\contactButton.png")

        background = canvas.create_image(800.0, 450.0, image=background_img)
        b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=lambda: self.convert(selected=2),
                    relief="flat")
        b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=lambda: self.convert(selected=0),
                    relief="flat")
        b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=lambda: self.convert(selected=1),
                    relief="flat")
        b3 = Button(bg='black', image=img3, borderwidth=0, highlightthickness=0, command=lambda: window.destroy(),
                    relief="flat")
        self.button = Button(image=contactImg, borderwidth=0, highlightthickness=0, command=lambda: self.contact(),
                    relief="flat",bg='#5A4517')
        b0.place(x=491.0, y=371.0, width=153, height=40)
        b1.place(x=491.0, y=430.0, width=153, height=40)
        b2.place(x=491.0, y=489.0, width=153, height=40)
        b3.place(x=1121.0, y=195.0, width=40, height=40)
        self.button.place(x=72,y=178)
        window.mainloop()

    def temp_entry0(self, e):
        if self.entry0.get() == "Enter here the text" or self.entry0.get() == "Enter here the Path of the File":
            self.entry0.delete(0, "end")

    def selectFile(self, file=False):
        self.file = file
        if file:
            if self.entry0:
                self.entry0.destroy()
            self.entry0 = Entry(justify='center', bd=7, bg="#AD0B34", highlightthickness=0,
                                font=('Times 14 italic bold'),
                                fg='black')
            self.entry0.insert(0, "Enter here the Path of the File")
            self.entry0.place(x=618.0, y=544.0, width=368, height=71)
            self.entry0.bind("<FocusIn>", self.temp_entry0)
        else:
            if self.entry0:
                self.entry0.destroy()
            self.entry0 = Entry(justify='center', bd=7, bg="#AD0B34", highlightthickness=0,
                                font=('Times 14 italic bold'),
                                fg='black')
            self.entry0.insert(0, "Enter here the text")
            self.entry0.place(x=618.0, y=544.0, width=368, height=71)
            self.entry0.bind("<FocusIn>", self.temp_entry0)

    def show(self, flag):
        """
        show UI Positive or Negative one
        """
        if self.win:
            self.win.destroy()
        window = self.win = Toplevel()
        window.geometry("803x492")
        window.configure(bg="#ffffff")
        canvas = Canvas(window, bg="#ffffff", height=492, width=803, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        if flag:  # true the Positive

            background_img = PhotoImage(master=window, file=path + r"\Positivebackground.png")
            background = canvas.create_image(400.5, 246.0, image=background_img)
        else:
            background_img = PhotoImage(master=window, file=path + r"\Negativebackground.png")
        background = canvas.create_image(400.5, 246.0, image=background_img)
        window.resizable(False, False)
        window.mainloop()

    def showFiles(self, dec):

        if self.win:
            self.win.destroy()
        ws = self.win = Toplevel()
        ws.title('PythonGuides')
        ws.geometry('1600x900')

        set = ttk.Treeview(ws)
        set.place(x=0, y=0, width=1600, height=900)

        set['columns'] = ('text', 'state')
        set.column("#0", width=0, stretch=NO)
        set.column("text", anchor=CENTER, width=80)
        set.column("state", anchor=CENTER, width=80)

        set.heading("#0", text="", anchor=CENTER)
        set.heading("text", text="text", anchor=CENTER)
        set.heading("state", text="state", anchor=CENTER)

        counter = 0
        for i in dec:
            set.insert(parent='', index='end', iid=counter, text='', values=(i, dec[i]))
            counter += 1

    def Enter(self, event):
        if self.file:
            try:
                f = open(self.entry0.get(), encoding='utf-8')
                l = []
                dec = {}
                for i in f.readlines():
                    l.append(i.replace('\n', ''))
                for s2 in l:

                    lstest = Module.PrePro(s2, Module.LSPosEmoji, Module.Love, Module.NegEmoji, Module.lsDoaa,
                                           Module.lsPosAG, Module.lsAngAS, Module.lsNegAB)
                    if self.selected == 0:
                        flag = (Module.DtreeMOd.predict([lstest]))
                    elif self.selected == 1:
                        flag = (Module.NaiveMOd.predict([lstest]))
                    else:
                        flag = (Module.NutNetMOd.predict([lstest]))
                    ans = None
                    if flag[0] == 1:
                        ans = 'Positive'
                    elif flag[0] == 0:
                        ans = 'Negative'
                    if ans:
                        dec[s2] = ans
                self.showFiles(dec=dec)

            except:
                pass

        else:  # 0 ==> Decision trees // 1 ==> Naïve Bayes // 2 ==> neural network
            s2 = ''
            if self.entry0.get() != "Enter here the text" and self.entry0.get() != "" and self.entry0.get():
                s2 = str(self.entry0.get())
                lstest = Module.PrePro(s2, Module.LSPosEmoji, Module.Love, Module.NegEmoji, Module.lsDoaa,
                                       Module.lsPosAG, Module.lsAngAS, Module.lsNegAB)
                if self.selected == 0:
                    flag = (Module.DtreeMOd.predict([lstest]))
                elif self.selected == 1:
                    flag = (Module.NaiveMOd.predict([lstest]))
                else:
                    flag = (Module.NutNetMOd.predict([lstest]))
                if flag == [0] or flag == [1]:
                    self.show(flag=flag[0])

    def exit(self, event):
        self.window.attributes('-fullscreen', False)


interface().start()
