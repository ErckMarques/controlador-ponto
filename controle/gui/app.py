from tkinter import Tk, Label


if __name__ == "__main__":
    app = Tk('teste inicial'.capitalize())
    Label(app, text='Este é um label na minha aplicação TKInter').pack()
    app.mainloop()